import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})


# API-ключ созданный ранее
token = '9061821dadd21ac576d9a19531c48df9b1856ef0567f6de38a3c1b190ed94742bf5afe744f536d4f506cc'

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)