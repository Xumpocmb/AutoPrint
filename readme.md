# Мониторинг папки и автоматическая печать файлов

Этот скрипт мониторит указанную папку на наличие новых файлов и автоматически отправляет их на печать, если они еще не были напечатаны. После успешной печати файл добавляется в базу данных, чтобы избежать повторной печати.

## Установка

1. Убедитесь, что на вашем компьютере установлен Python версии 3.x.
2. Клонируйте этот репозиторий на свой компьютер.
3. Установите зависимости, выполнив следующую команду в терминале:

```
pip install -r requirements.txt
```

## Использование

1. Отредактируйте переменные `folder_to_watch` и `db_file` в файле `monitor_folder.py`, чтобы указать папку для мониторинга и путь к файлу базы данных соответственно.
2. Запустите скрипт, выполнив его команду в терминале:

    ```
    python monitor_folder.py
    ```

3. Скрипт начнет мониторинг указанной папки. При обнаружении новых файлов он автоматически отправит их на печать, если они еще не были напечатаны.

## Зависимости

Скрипт использует следующие библиотеки Python:

- `os`: Для работы с файловой системой.
- `sqlite3`: Для работы с базой данных SQLite.
- `time`: Для создания задержек между проверками папки и печатью.

## Дополнительные сведения

- Для корректной работы скрипта убедитесь, что принтеры, указанные в переменных `printer1_name` и `printer2_name` в файле `print_file.py`, доступны и готовы к печати.
