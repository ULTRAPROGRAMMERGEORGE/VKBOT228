param2 = {'access_token': token, 'user_id': m, 'v': 5.131, 'fields': m, 'message': f'Это твоя жертва{c,d}'}
rec4 = requests.get(url=f'https://api.vk.com/method/{method3}', params=param2)
rec3 = requests.get(url=f'https://api.vk.com/method/{method2}', params=param20)
method3 = 'messages.send'
rec3 = requests.get(url=f'https://api.vk.com/method/{method2}', params=param20)
print(m,b)
c = b.get('first_name')
d = b.get('last_name')
print(c,d)
param20 = {'access_token': token, 'chat_id': 95, 'v': 5.131,'fields':'nickname'}
https://oauth.vk.com/authorize?client_id=51526354&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&messages&groups&response_type=token&v=5.131
vk1.a.zeWsqRWLjl8xVHciw-VyoZ6EM5FQP2kAWv9NFFZNXvQJaxdskpidyMO_8xlhgW7w9MGBLPdunTOy7jZhTo-OcAHmDjN6Tln1GJabVKlo-Nfve2Dek0J_EXm96oAVrJd1iqAFB2pQ6phjvKJegoNz2gxwTaaEX1UWAU5dwQQXHb0M55zPQXKz6AiHV4WgZP9Q
for i in range(len(rec2.json()['response']['items'])):
    e=rec2.json()['response']['items'][j].get('id')
    o.append(e)

    j += 1
m = o[randrange(0, len(o))]
print(m)
for name in range(len(rec3.json())):
    nick.append(rec3.json())
    lick += 1
b = nick[randrange(0, len(nick))]
c = b.get('first_name')
d = b.get('last_name')
param2 = {'access_token': token, 'user_id': s, 'v': 5.131, 'message': f'Это твоя жертва{c,d}'}

param20 = {'access_token': token, 'chat_id': idiks, 'v': 5.131,'fields':'nickname'}
def create_cht(users_id,title):
    vk.method('messages.createChat', {'user_ids': users_id,'title': title})