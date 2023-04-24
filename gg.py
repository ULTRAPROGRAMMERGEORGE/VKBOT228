def tainii():
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.from_chat:

                request = event.text

                if request == "у":
                    write_msg(event.chat_id, "Хай")
                    full_name = get_name()
                    spisok.append(full_name)
                    spi.append()
                elif request == 'итоги':
                    spisok1()
                    write_msg(event.chat_id, f'Вот твоя жертва,{spisok1()}')




def invite_bot(user_id):
    data2 = gh.method('messages.isMessagesFromGroupAllowed', {'group_id': group_id, 'user_id': user_id})[0]
    return "{} {}".format(data2['is_allowed'])


def write_msg(chat_id, message):
    gh.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': 0})


def write_msgu(user_id, message):
    gh.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})


def get_name(chat_id: int) -> str:
    data = gh.method("messages.getChatUsers", {"chat_id": chat_id})[0]
    return "{} {}".format(data["first_name"], data["last_name"])


def spisok1():
    bimba = randrange(0, len(spisok))
    bomba = randrange(0, len(spi))


def tainii():
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.from_chat:

                request = event.text

                if request == "у":
                    write_msg(event.chat_id, "Хай")
                    full_name = get_name()
                    spisok.append(full_name)
                    spi.append()
                elif request == 'итоги':
                    spisok1()
                    write_msg(event.chat_id, f'Вот твоя жертва,{spisok1()}')
            elif event.from_user:

                request = event.message

                if request == "у":
                    write_msgu(event.user_id, "Хай")
                    full_name = get_name()
                    spisok.append(full_name)
                    spi.append()
                elif request == 'итоги':
                    spisok1()
                    write_msgu(event.user_id, f'Вот твоя жертва,{spisok1()}')


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        if event.from_chat:

            request = event.message

            if request == 'start':
                tainii()
            else:
                write_msg(event.chat_id, 'команды')
        elif event.from_user:

            request = event.message

            if request == 'start':
                tainii()
            else:
                write_msgu(event.user_id,'команды')
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:

                if event.from_user:
                    request = event.text
                    user_id = event.user_id
                    if request == 'start':
                        server1.send_msg(user_id,'III')

                elif event.from_chat:
                    request = event.text
                    chat_id = event.chat_id
                    if request == 'start':
                        server1.send_message(chat_id,'III')
    except Exception as error:
        print(error)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.id > 0:
                request = event.text
                user_id = event.user_id
                if request == 'start':
                    server1.send_message(user_id, 'III')
            else:
                request = event.text
                chat_id = event.chat_id
                if request == 'start':
                    server1.send_message(chat_id, 'III')
self.vk_api.users.get(user_id=user_id)
jertvi=dict([user_id,server1.get_user_name(user_id)])
                        print(jertvi)
server1.send_msg(spisok[randint(0, len(spisok))], f'Воот он {d.get(j)}')
