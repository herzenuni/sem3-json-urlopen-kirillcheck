# Шахов Кирилл
# Задание - На основе кода с выполнением предыдущего задания (см. тему 18) 
# реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран (через функцию). 

from urllib.request import urlopen 
import pprint
import json


def hacker_man(id):   # на вход подаём цифру-id пользователя на выходе имеем некоторые основные данные (возможен вывод большего числа данных)
    inquiry = "https://api.vk.com/method/users.get?user_ids={id}&fields=education&v=5.69".format(id = id)

    try:     """ отлавливание исключений  """
        inquiry_obj = urlopen(inquiry)  """ отправка запроса на сервер""" 
        obj = json.loads(inquiry_obj.read())   """ перевод в json"""
    except:
        print('Ошибка соединения')
    return obj


if __name__ == "__main__":  """штучка для прямой работы программы (по порядку)"""
    id = input(' Введите id: \n')
    print('Ответ сервера: \n')
    pprint.pprint(hacker_man(id))
