
import requests
import json
# Обычно к открытым API прилагается подробная документация, где описывается логика формирования ссылок и какие данные
# по ним можно получать (или отправлять!).

# Изучите документацию того же сайта по «Звёздным войнам».
#
# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее. А ещё попробуйте библиотеку swapi
# (о ней также в документации) и с её помощью выведите начало сюжета из фильма «Новая надежда» (A New Hope).

# my_req = requests.get('https://google.com/')
# print(my_req.text)

# my_req = requests.get('https://swapi.dev/api/people/3/')
# #print(my_req.text)
#
# data = json.loads(my_req.text)         # десериализация JSON
# data['name'] = 'Denis'
# print(data['name'])
# print(data['homeworld'])
#
# with open('my_test.json', 'w') as f:
#     json.dump(data, f, indent=4)       # сереализация JSON
#
# with open('my_test.json', 'r') as f:
#     data = json.load(f)
#
# print(data)



# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/1/")

json_dict = json.loads(result.text)

print(json_dict["opening_crawl"])