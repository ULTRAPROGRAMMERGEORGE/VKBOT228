from random import randrange
from threading import Thread

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

group_id = 209144032
spisok = []
spi = []
j = 0
tokenjopan = 'vk1.a.5qKt00n1qIIors3n7YaezaXwN-Wnw52--Yh8R5bFINYlvqa-U2DUVDhnxLR3-UalrhF8B-TKYn3z5AWj_G9roELAUjyynuE3XBZ1DWlxNepS0APxfhcPg7mNnvgIMzWKXkqF_EHoIaEXGoaqNBmQ9SUEKxeqi0NzlbIJ3UNgKCh2yavyz4QJRiaOFtyxfRRJwCh5JwzenhUTfenkv_LCcw'
gh = vk_api.VkApi(token=tokenjopan)
longpoll = VkBotLongPoll(gh, group_id=group_id)


def spisok1():
    bimba = randrange(0, len(spisok))
    bomba = randrange(0, len(spi))


class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def invite(self, chat_id):
        self.vk_api.messages.allowMessagesFromGroup(group_id=group_id)

    def invite2(self):
        self.vk_api.groups.getLongPollServer(group_id=group_id)

    def send_msg(self, user_id, message):
        self.vk_api.messages.send(peer_id=user_id, user_id=user_id, message=message, random_id=0)

    def send_message(self, chat_id, message):
        self.vk_api.messages.send(peer_id=2000000000 + int(chat_id), chat_id=int(chat_id), message=message, random_id=0,
                                  group_id=group_id)

    def get_user_name(self, user_id):
        return user_id

    def get_name(self, chat_id, kok):
        return self.vk_api.messages.getConversationMembers(peer_id=2000000000 + int(chat_id), chat_id=int(chat_id))[
            'profiles'][kok]['id']

    def get_id(self, user_ids,kok):
        return self.vk_api.users.get(user_ids=user_ids)['profiles'][kok]['id']

    def get_name20(self, chat_id, kok):
        return self.vk_api.messages.getConversationMembers(peer_id=2000000000 + int(chat_id), chat_id=int(chat_id))[
            'profiles'][kok]['first_name']

    def get_name30(self, chat_id, kok):
        return self.vk_api.messages.getConversationMembers(peer_id=2000000000 + int(chat_id), chat_id=int(chat_id))[
            'profiles'][kok]['last_name']

    def kol_vo(self, chat_id):
        return self.vk_api.messages.getConversationMembers(peer_id=2000000000 + int(chat_id), chat_id=int(chat_id))[
            'count']

    def online(self):
        self.vk_api.groups.enableOnline(group_id=group_id)

