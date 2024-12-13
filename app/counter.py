def read_file_lines(filename):
    """
    Функция для чтения строк из файла и возврата их в виде списка.
    
    :param filename: Имя файла для чтения
    :return: Список строк из файла или пустой список в случае ошибки
    """
    try:
        # Открываем файл для чтения с кодировкой UTF-8
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().splitlines()  # Читаем все строки и возвращаем их в виде списка
    except Exception as exc:
        # Обработка исключений при чтении файла
        print(f"\nПри чтении файла: {filename} возникла ошибка: {exc}\n")
        return []  # Возвращаем пустой список в случае ошибки

def write_to_file(texts: dict, filename):
    """
    Функция для записи слов и их подсчётов в файл.
    
    :param texts: Словарь, содержащий слова и их количество
    :param filename: Имя файла для записи
    """
    try:
        # Открываем файл для записи с кодировкой UTF-8
        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in texts.items():
                # Записываем каждую пару "слово: количество" в новую строку
                file.write(f"{key}: {value}\n")
    except Exception as exc:
        # Обработка исключений при записи в файл
        print(f"\nПри записи в файл: {filename} возникла ошибка: {exc}\n")

# Загрузка списка слов и фраз для подсчёта из файла 'words.txt'
words_list = read_file_lines('words.txt')

# Создание словаря для подсчёта, инициализируем каждое слово с нулевым значением
word_counts = {word: 0 for word in words_list}

# Функция подсчёта слов в тексте
def count_words_in_text():
    """
    Функция для подсчёта количества вхождений слов из списка в тексте.
    """
    print('Подсчёт слов')
    # Открываем файл с собранными текстами для чтения
    with open('collected_texts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Читаем все строки из файла
        # Перебираем каждую строку в файле
        for line in lines:
            # Перебираем каждое слово из загруженного списка
            for word in words_list:
                # Если слово найдено в строке
                if word in line:
                    word_counts[word] += 1  # Увеличиваем его счётчик на 1
    # Записываем результаты подсчёта в файл 'word_counts.txt'
    write_to_file(word_counts, 'word_counts.txt')
