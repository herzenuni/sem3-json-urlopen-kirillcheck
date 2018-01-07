# сделал - Галкин Антон 2 курс ИВТ
# тест для URL 

import URL_def

def test_1():
    assert URL_def.user_vk(1).get('response[0]') == 'Павел'
