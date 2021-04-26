from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot.vk_bot import VkBot, vk

longpoll = VkLongPoll(vk)
print('Сервер запущен...')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('Новое сообщение от пользователя ' + str(event.user_id) + ':')
            print('    ' + event.text)
            bot = VkBot(event.user_id)
            print('Ответ: ')
            print('    ' + bot.new_message(event.text))
            answer = bot.new_message(event.text)
            bot.write_msg(answer)
