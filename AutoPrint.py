import os
import time
import sqlite3
from print_file import print_pdf

db_file = 'printed_files.db'
folder_to_watch = 'D:/Desktop/тест/'


def create_database():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS printed_files (file_name TEXT PRIMARY KEY)''')
    conn.commit()
    conn.close()


def add_printed_file(file_name):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("INSERT INTO printed_files (file_name) VALUES (?)", (file_name,))
    conn.commit()
    conn.close()


def is_file_printed(file_name):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM printed_files WHERE file_name=?", (file_name,))
    result = c.fetchone()
    conn.close()
    return result is not None


if __name__ == '__main__':
    print('Скрипт запущен')
    create_database()
    try:
        # Основной цикл мониторинга папки
        while True:
            # Получение списка файлов в папке
            files = os.listdir(folder_to_watch)
            for file in files:
                file_path = os.path.join(folder_to_watch, file)
                if os.path.isfile(file_path) and not is_file_printed(file):
                    # Отправка файла на печать
                    print(f"Печать файла: {file_path}")
                    print_pdf(file_path)
                    add_printed_file(file)
            # Пауза перед следующей проверкой
            time.sleep(5)  # Проверка каждые 5 секунд
    except KeyboardInterrupt:
        print("Программа завершена.")
