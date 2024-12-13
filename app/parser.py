import requests  # Импортируем библиотеку для работы с HTTP-запросами
import random    # Импортируем библиотеку для генерации случайных чисел
import time      # Импортируем библиотеку для работы с временем
from config import TOKEN # Импортируем секретный токен

# Список для хранения собранных текстов постов
collected_texts = []

def random_delay(min_delay=0.5, max_delay=1.5):
    """
    Функция для создания случайной задержки между запросами.
    
    :param min_delay: Минимальная задержка (в секундах)
    :param max_delay: Максимальная задержка (в секундах)
    """
    time.sleep(random.uniform(min_delay, max_delay))  # Задержка на случайное время

def write_to_file(texts, filename):
    """
    Функция для записи собранных текстов в файл.
    
    :param texts: Список текстов для записи
    :param filename: Имя файла, в который будет произведена запись
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for text in texts:
            file.write(text + '\n')  # Записываем каждый текст в новую строку

# Переменная для хранения токена доступа к API ВКонтакте


def parser():
    """
    Функция для парсинга постов из сообщества ВКонтакте.
    """
    endpoint_url = 'https://api.vk.com/method/wall.get'  # URL для запроса к API
    domain = "smeshariki"  # Домен сообщества, откуда будем извлекать посты
    version = "5.199"  # Версия API
    count = 100  # Количество постов, которые будут запрашиваться за один раз

    # Переменная для сбора постов
    collected_texts = []

    # Цикл для получения постов с использованием смещения
    for offset in range(0, 100000, count):  # Смещение увеличивается на количество постов
        params = {
            'access_token': TOKEN,  # Токен доступа
            'v': version,  # Версия API
            'domain': domain,  # Домен сообщества
            'offset': offset,  # Смещение для получения следующей порции постов
            'count': count  # Количество постов для запроса
        }
        
        # Выполняем GET-запрос к API
        response = requests.get(url=endpoint_url, params=params)

        # Проверяем, успешно ли выполнен запрос
        if response.status_code == 200:
            data = response.json()  # Преобразуем ответ в JSON-формат
            # Проверяем наличие 'response' и 'items' в данных
            if 'response' in data and 'items' in data['response']:
                for post in data['response']['items']:
                    text = post.get('text', '').strip()  # Извлекаем текст поста и убираем лишние пробелы
                    if text:  # Проверяем, что текст не пустой
                        collected_texts.append(text)  # Добавляем текст в список
            else:
                print(f"Проблема с ответом API: {data}")  # Выводим сообщение об ошибке, если данные некорректные
        else:
            print(f"Ошибка запроса: {response.status_code}")  # Выводим код ошибки, если запрос не успешен
            break  # Прекращаем парсинг при ошибке

        random_delay()  # Задержка между запросами для избежания ограничения по частоте запросов

    # Записываем собранные тексты в файл
    write_to_file(collected_texts, 'collected_texts.txt')

