from random import randint
from threading import Thread
from vk_api import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from config import vk_api_token
from main import Server

d = {}
p = True


def sbor_infi(chat_id, kok):
    c = server1.get_name20(chat_id, kok) + ' \t ' + server1.get_name30(chat_id, kok)
    d[server1.get_name(chat_id, kok)] = c
    xyi[kok] = server1.get_name(chat_id, kok)
    print(xyi)


group_id = 209144032
tokenjopan=''
gh = vk_api.VkApi(token=tokenjopan)
server1 = Server(vk_api_token, 209144032, "server1")
long_poll = VkBotLongPoll(gh, group_id)
spisok = []
simpl = []
spisok2 = []
xyi = {}
while True:
    if __name__ == '__main__':
        def priem():
            try:
                for event in long_poll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if event.from_chat:
                            chat_id = event.chat_id
                            if event.message['text'].lower() == 'start':
                                server1.send_message(chat_id, 'III')
                                kol = int(server1.kol_vo(chat_id)) - 1
                                for kok in range(0, kol):
                                    sbor_infi(chat_id, kok)
                                break
                            else:
                                for i in range(0, 2):
                                    server1.send_message(chat_id, 'Я хуй')
            except Exception as error2:
                print(error2)
            except KeyboardInterrupt as error1:
                print(error1)


        def poluchi():
            try:
                for event in long_poll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if event.from_user:
                            user_id = event.object.message['from_id']
                            if event.message['text'].lower() == 'start':
                                for j in range(0,len(xyi)):
                                    poping=randint(0,len(xyi)-1)
                                    server1.send_msg(user_id, f'{d.get(xyi.get(poping))}')
                                    xyi.pop(poping)
                                    d.pop(xyi.get(poping))
                                    print(xyi,d)
                            else:
                                server1.send_msg(user_id, 'II')
            except Exception as error2:
                print(error2)
            except KeyboardInterrupt as error1:
                print(error1)

        priem()
        poluchi()