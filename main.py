import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import *
import json

from Vk_bot import *

vk = vk_api.VkApi(token=token1, api_version='5.125')
#vk.auth()
longpoll = VkBotLongPoll(vk, group_id=group_id_1, wait=25)
api = vk.get_api()

def write_msg(user_id,message, keyboards = None):
    api.messages.send(user_id = user_id, random_id = 0, message = message, keyboard = keyboards)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_user:
            if event.object['message']['text'] == 'Начать':
                vk_bot = VkBot(str(event.object['message']['from_id']))
                write_msg(event.object['message']['from_id'], message='Приветствуем тебя! Мы рады видеть тебя в нашей группы! Тыкай на клавиатуру чтобы получить дополнительную информацию!', keyboards=vk_bot.get_keyboard())
            else:
                print(f"Message from {event.object['message']['from_id']}")
                print(f"Body of message {event.object['message']['text']}")
                vk_bot = VkBot(str(event.object['message']['from_id']))
                write_msg(event.object['message']['from_id'], message=vk_bot.new_messg(event.object['message']['text']),)


