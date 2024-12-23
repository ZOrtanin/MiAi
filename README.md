# Помощник для заметок в Obsidian

## Обзор

Этот Python-скрипт взаимодействует с API Mistral AI для симуляции разговора с виртуальным помощником по имени Лиза. Скрипт читает настройки конфигурации из файла `config.ini`, отправляет сообщения пользователя в API Mistral AI и сохраняет определенные заметки в Obsidian на основе команд пользователя.

## Функции

- **Чтение конфигурации**: Читает API-ключ и путь к Obsidian из файла `config.ini`.
- **Управление диалогом**: Поддерживает историю разговора с виртуальным помощником.
- **Сохранение заметок**: Автоматически сохраняет заметки в Obsidian при триггере определенных команд пользователя.
- **Обработка ошибок**: Проверяет доступность файла для чтения и обрабатывает ошибки ответов API.

## Требования

- Python 3.x
- Библиотека `requests`
- Библиотека `configparser`
- Библиотека `os`
- Библиотека `datetime`

## Установка

1. **Клонируйте репозиторий**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Установите зависимости**:
	```sh
	pip install requests
	```

3. **Создайте файл config.ini:**
	```sh
	[api]
	key = your_mistral_api_key

	[os]
	path_to_obsidian = your_obsidian_path
	```

## Использование

1. **Запустите скрипт:**
	```sh
	python script_name.py
	```

2. **Взаимодействуйте с Лизой:**
	- Введите свои сообщения после приглашения Я: .
	- Лиза будет отвечать на основе истории разговора.
	- Чтобы сохранить заметку в Obsidian, включите фразу "Добавь это в заметку Осидиан" или любую ее вариацию в свое сообщение.

