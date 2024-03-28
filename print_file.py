import os
from time import sleep
import win32api
import win32print

printer1_name = "Canon LBP2900"
printer2_name = "Canon LBP2900"


def print_pdf(pdf_file_path):
    # печать на 1ом принтере
    print('*' * 30)
    print(f'Делаю задачу печати на {printer1_name} принтере')
    win32print.SetDefaultPrinter(printer1_name)
    print(f"Файл для печати: {pdf_file_path}")
    win32api.ShellExecute(0, "print", pdf_file_path, win32print.GetDefaultPrinter(), ".", 0)
    # subprocess.Popen([r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe", "/N", "/T", pdf_file_path])

    sleep(30)
    # печать на 2ом принтере
    print('*' * 30)
    print(f'Делаю задачу печати на {printer2_name} принтере')
    win32print.SetDefaultPrinter(printer2_name)
    print(f"Файл для печати: {pdf_file_path}")
    win32api.ShellExecute(0, "print", pdf_file_path, win32print.GetDefaultPrinter(), ".", 0)
    # subprocess.Popen([r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe", "/N", "/T", pdf_file_path])

    # настройка принтера по умолчанию
    win32print.SetDefaultPrinter(printer1_name)
    print('Печать завершена. Настройки принтера установлены по умолчанию.')


if __name__ == "__main__":
    print("-" * 30)
