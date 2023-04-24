try:
    from random import randrange
    import requests
    import vk_api
    import vkapi
    from vk_api.longpoll import VkLongPoll, VkEventType

    token=''
    tokenjopa=''
    vk = vk_api.VkApi(token=tokenjopa)


    def write_msg(user_id, message):
        vk.method('messages.send', {'user_id': user_id, 'message': message})


    o = []
    nick = []
    j = 0
    lick = 0
    index = 1
    kok = 0
    v = []
    s = []

    title = 'test'
    method = 'messages.createChat'
    method2 = 'messages.getChat'
    method4 = 'groups.getMembers'
    method5 = 'groups.create'
    param5 = {'access_token': token, 'title': 'test', 'type': 'group', }
    p = {'access_token': token, 'group_id': 213563737, 'v': 5.131, 'fields': 'users_id'}
    rec2 = requests.get(url=f'https://api.vk.com/method/{method4}', params=p)
    for i in range(len(rec2.json()['response']['items'])):
        o.append(rec2.json()['response']['items'][j].get('id'))
        j += 1
    param20 = {'access_token': token, 'group_id': 213563737, 'v': 5.131, 'fields': 'nickname'}
    rec3 = requests.get(url=f'https://api.vk.com/method/{method4}', params=param20)
    for name in range(len(rec3.json()['response']['items'])):
        nick.append(rec3.json()['response']['items'][lick])
        lick += 1
    longpoll = VkLongPoll(vk)
    for comp in range(len(o)):
        c1 = randrange(0, len(o))
        m = o[c1]
        print(m)
        g = randrange(0, len(nick))
        b = nick[g]
        c = b.get('first_name')
        d = b.get('last_name')
        print(c, d)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:

                # Если оно имеет метку для меня( то есть бота)
                if event.to_me:

                    # Сообщение от пользователя
                    request = event.text

                    # Каменная логика ответа
                    if request == "хочу":
                        write_msg(event.user_id, f"Хай,вот твоя жертва{c, d}")

                    elif request == "Хочу":
                        write_msg(event.user_id, f"Хай,вот твоя жертва{c, d}")

                    else:
                        continue
except KeyboardInterrupt:  # Исключение при становке пользователем
    print(
        'Завершено пользователем [OK]')  # Выводим сообщение о том, что программа завершена пользователем, стирая строку с символами Ctrl+C
except ValueError:  # Ошибка при попытке отправки сообщения пользователю, которому вы не можете отправлять сообщения
    print(
        'Возникла ошибка при попытке отправить сообщение указанному адресату [ERROR]')  # Выдаем соответствующее уведомление
