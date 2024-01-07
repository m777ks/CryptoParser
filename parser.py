import random
import json
import requests
from fake_useragent import UserAgent
from time import sleep

useragent = UserAgent()
# Создаем фаил JSON ключами(названием монет) и передаем его переменной
with open('prices.json', encoding='utf-8') as file:
    keys_all = json.load(file)

# Создаем счетчик и выводим количество монет из списка
coin = 0
number_of_requests = len(keys_all['data']) - 1
print(number_of_requests)

# С помощью цикла перебираем монеты
for key in keys_all['data']:

    # Использовал данные своего агента, но можно и fake
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'x-nextjs-data': '1'
    }
    # Использую ссылку с сайта для обращение к нужной монете через его api
    req = requests.get(
        url=f'https://api.cryptorank.io/v0/team/by-coin-key/{key["key"]}',
        headers=headers)
    # Выводим текущий статус и запрос, если 404 то у монеты нет вкладки team
    print(f'#{coin} Название монеты: {key["key"]} статус запроса: {req.status_code}')
    total = 1
    if req.status_code != 404:
        src = req.json()
        #  Записываем json на комп
        with open(f'data/{key["key"]}test.json', 'w', encoding='utf-8') as file:
            json.dump(src, file, indent=4, ensure_ascii=False)
        total += 1
        print(f'Выполнено {total} запросов из {number_of_requests}')

    coin += 1
    sleep(random.randint(2, 4))


