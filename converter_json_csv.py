import os
import json
import csv

# Открываем папку с json файлами
files = r'C:\Users\HP\Desktop\bots\CryptoParser\data'
test = os.listdir(files)

# Создаем файл таблицы и называем столбцы
with open(f'csv/pars.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow((
        'token_name',
        'token_href',
        'name',
        'profession',
        'link'
    ))

quantity = len(test)

coin = 0
# С помощью цикла перебираем файлы и забираем нужные данные
for name in test:
    coin += 1
    with open(f"data/{name}", encoding='utf-8') as file:
        token = json.load(file)
        # print(token)
        token_name = name.replace('test.json', '')

        print(token_name, coin )
        token_href = 'https://cryptorank.io/price/' + token_name
        # print(token_href)
        for user in range(len(token['data'])):
            name = token['data'][user]['name']
            # print(name)
            jobs = token['data'][user]['jobs']
            # print(jobs)
            links = token['data'][user]['links']
            # print(links)

            with open(f'csv/pars.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow((
                    token_name,
                    token_href,
                    name,
                    jobs,
                    links
                ))





