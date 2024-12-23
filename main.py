import requests
import os
import configparser
from datetime import datetime

file_path = "config.ini"

config = configparser.ConfigParser()
files = config.read(file_path)

API_key = config['api']['key']
path_obsidian = config['os']['path_to_obsidian']

dialog = [
            {"role": "user", "content": "Привет можешь взять на себя роль девушки по имени Лиза"},
            {"role": "assistant", "content": "Привет! Конечно, я могу взять на себя роль Лизы. Как я могу помочь?"},
            {"role": "user", "content": "Привет как тебя зовут?"},
            {"role": "assistant", "content": "Привет! Меня зовут Лиза. А тебя как зовут?"},
            {"role": "user", "content": "Егор"},
            {"role": "assistant", "content": "Привет, Егор! Рада познакомиться. Как я могу помочь?"},
            {"role": "user", "content":"можешь после моих слов 'Добавь это в заметку Осидиан' и все производные этой фразы отвечать 'Хорошо добавляю это в заметку Обсидиан'"},
            {"role": "assistant", "content": "Конечно, Егор! Давай попробуем. Говори свои слова, а я буду отвечать соответствующим образом."}
            
        ]

def files_read_error():
    if os.access(file_path, os.R_OK) == False:
        print("config.ini Не доступен для чтения:", os.access(file_path, os.R_OK))
    if files == []:
        print("Не удалось прочитать config.ini")

    print('... Файлы прочитанны ...')

def getDate():
    # Получаем текущую дату и время
    current_datetime = datetime.now()

    # Форматируем дату и время в строку
    formatted_datetime = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")

    return formatted_datetime

def addObsidian(note_content):
    note_title = getDate()

    path = os.path.expanduser('~/Documents/obsidian/база_знаний/заметки_от_Лизы/'+ str(note_title) + '.md')
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Открываем файл для записи
    with open(path, 'w', encoding='utf-8') as file:
        file.write(note_content)

    print(f"Заметка '{note_title}' успешно добавлена в Obsidian.")

def send(dialog):

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer "+API_key
    }
    data = {
        "model": "mistral-large-latest",
        "stream": False,
        "messages": dialog
    }



    response = requests.post(url, headers=headers, json=data)


    # Проверяем ответ
    if response.status_code == 200:
        result = response.json()['choices'][0]['message']['content']
        print('Лиза: '+ result)
        dialog.append({"role": "assistant", "content":  result })
        print('')

    else:
        result = ''
        print(f"Ошибка: {response.status_code}")
        print(response.text)

    return result

files_read_error()

while True:
    text = input('Я: ')
    dialog.append({"role": "user","content": text })
    answer = send(dialog)

    if 'Хорошо, добавляю это в заметку Обсидиан.' in answer :
        #print('save: \n' + dialog[-3]["content"])
        addObsidian(dialog[-3]["content"])





