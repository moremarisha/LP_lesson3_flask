import requests
from constants import data_mos_key

site_adress = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key='+data_mos_key
print(site_adress)
res = requests.get(site_adress)
print('код ответа: %s' % res)
print('код ответа int: %s' % res.status_code)
print('заголовок: %s' % res.headers)
print('содержимое: %s' % res.text)
print('кодировка: %s' % res.encoding)