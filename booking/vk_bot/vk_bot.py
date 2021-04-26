import requests
import bs4
import vk_api
from vk_bot.settings import TOKEN
from server import Handler
from server.data import db_session
import json

vk = vk_api.VkApi(token=TOKEN)
db_session.global_init("../server/data/db/cinema.db")
Handler.get_films()
with open("films.json", "rt", encoding="utf8") as f:
    films_list = json.loads(f.read())


class VkBot:

    def __init__(self, user_id):
        global films_list
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА", "БРОНЬ", "РАСПИСАНИЕ", "КОМАНДЫ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    # Получение времени:
    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    # Получение погоды
    def _get_weather(self, city: str = "санкт-петербург") -> list:
        request = requests.get("https://sinoptik.com.ru/погода-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")

        p3 = b.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = b.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = b.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = b.select('.temperature .p6')
        weather4 = p6[0].getText()
        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = b.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result

    def new_message(self, message):
        MESSAGE = message.upper()
        # Привет
        if MESSAGE == self._COMMANDS[0]:
            return f"Здравсвуйте, {self._USERNAME}. Чтобы посмотреть список фильмов, напиши 'расписание'," \
                   f" чтобы обормить бронь - 'бронь'!"

        # Погода
        elif MESSAGE == self._COMMANDS[1]:
            return self._get_weather()

        elif MESSAGE == self._COMMANDS[4]:
            return 'Бронь можно оформить тут:\nhttp://127.0.0.1:8080/'

        # Время
        elif MESSAGE == self._COMMANDS[2]:
            return self._get_time()

        elif MESSAGE == self._COMMANDS[5]:
            res = ['Расписание фильмов:\n', 'Название, Дата, Время, Цена, Зал\n', '\n']
            Handler.get_films()
            with open("films.json", "rt", encoding="utf8") as f:
                films_list = json.loads(f.read())
            films = films_list['films']
            for i in films:
                res.append(i['info'][:-2] + '\n')
            return ''.join(res)
        elif MESSAGE == self._COMMANDS[3]:
            return f"Пока-пока, {self._USERNAME}!"

        elif MESSAGE == self._COMMANDS[6]:
            return 'Список моих команд:\n' + ' Бронь\n' + ' Расписание\n'
        else:
            return "Не понимаю о чем вы..."

    def write_msg(self, message):
        vk.method('messages.send', {'user_id': self._USER_ID, 'message': message, 'random_id': 0})

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
