import logging  # Импортируем модуль для ведения логов
from app.parser import parser  # Импортируем функцию парсинга из модуля parser
from app.counter import count_words_in_text  # Импортируем функцию подсчёта слов из модуля counter

# Основная функция
def run():
    """
    Функция для запуска процесса парсинга и подсчёта слов.
    """
    try:
        # Вызываем функцию парсинга для получения текстов постов (если нужно)
        # Закомментировано, так как тексты всех постов уже получены
        # parser() 
        
        count_words_in_text()  # Вызываем функцию для подсчёта слов в собранных текстах
    except Exception as e:
        # Логируем ошибку, если что-то пошло не так
        logging.error(f"Произошла ошибка:\n{e}")

# Безопасный запуск
if __name__ == "__main__":
    run()  # Запускаем основную функцию, если файл исполняется как основной
