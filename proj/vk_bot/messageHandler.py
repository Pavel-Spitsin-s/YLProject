import vkapi
import os
import importlib
from command_system import command_list

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body, user_id):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    for c in command_list:
        if body.split()[0].lower() in c.keys:
            message = c.process(body, user_id)
    return message, attachment

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'], user_id)
   vkapi.send_message(user_id, token, message, attachment)