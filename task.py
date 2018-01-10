from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError 
import json
import pprint
import pytest


def InputVkIds():
  print('Введите список id, через запятую:')
  id = input()
  return id

def SendRequestVk(ids,url):
  request = url.format(id = ids)
  print('Сформированный запрос:', request)
  obj={}   
  try:
      request_obj = urlopen(request)#отправка на сервер
      obj = json.loads(request_obj.read())#конвертируем ответ сервера в JSON
  except URLError:
      raise      
  except HTTPError:
      raise      
  return obj

def JsonConsoleWriter(json):
  if (json.get('response') != None and json.get('response')!="error"):#двойная проверка JSON 1: для случая когда сервер отработал запрос, но вернул JSON с ошибкой в котором нет поля response 2: для случая когда сервер вообще ничего не вернул, это вариант exept 
      print('Ответ сервера:')
      resp=json.get('response')#складываем в переменную значение поля response
      for field in resp:
          print(' ' + '_'*70 + '\n')
          print(" First name: " + str(field['first_name']))
          print(" Last name: " + str(field['last_name']))
          print(" Nickname: " + str(field['nickname']))
          print(" Status: " + str(field['status']))
          print(" Online: " + str(field['online']))
          print(" Sex: " + str(field['sex']))
          print(" Last_seen: " + str(field['last_seen'])+ '\n')
          print(' ' + '_'*70 + '\n')      
  else:
    if (json.get('response') != None):
  	  if (json.get('error') != None):
  	  	print('Сервер вернул ошибку:')
  	  	pprint.pprint(json['error'])
  	  else:
  	  	print('Неизвестная ошибка!');
    else:
  	  resp=json.get('response')
  	  print(resp);

        
#JsonConsoleWriter(SendRequestVk(InputVkIds(),"https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site,first_name,last_name,status,online,last_seen&v=5.69"))
class TestList:

    def test_type_error(self):
        with pytest.raises(URLError):
            SendRequestVk("id150534032","https://jjr.jjr.jjr/method/users.get?user_ids={id}&fields=nickname,sex,city,site,first_name,last_name,status,online,last_seen&v=5.69")
    def test_check1(self):
        aa=SendRequestVk("id150534032","https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site,first_name,last_name,status,online,last_seen&v=5.69")
        assert (aa.get('response') != None)
    def test_check2(self):
        aa=SendRequestVk("asdasfdfdas","https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site,first_name,last_name,status,online,last_seen&v=5.69")
        assert (aa.get('error') != None)        
            
