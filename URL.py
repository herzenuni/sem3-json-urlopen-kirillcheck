# Шахов Кирилл
# ИВТ 2  курс 
# Задание - На основе кода с выполнением предыдущего задания (см. тему 18) 
# реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран. 


from urllib.request import urlopen # для url запроса
import json 
import pprint #красивый вид

print('Введите id:')  
id = input()    # на вход подаём цифру-id пользователя на выходе имеем некоторые основные данные
hacker_man = "https://api.vk.com/method/users.get?user_ids={id}&fields=education&v=5.69".format(id = id)
f1 = urlopen(hacker_man)

obj = json.loads(f1.read())
print(hacker_man)
print('')
pprint.pprint(obj
