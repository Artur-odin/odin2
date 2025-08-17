import tkinter as tk
from tkinter import messagebox

def study_radio():
    """Изучение радиокнопок"""
    window = tk.Toplevel()#есди просто Tk, то на других кнопках будут точки
    window.title("Радиокнопки")
    window.geometry("300x200")

    var = tk.StringVar(value="python")
    tk.Label(window, text="Выберите язык:").pack(pady=5)
    tk.Radiobutton(window, text="Python", variable=var, value="python").pack()
    tk.Radiobutton(window, text="Java", variable=var, value="java").pack()
    tk.Radiobutton(window, text="C++", variable=var, value="cpp").pack()


    def show_value():
        messagebox.showinfo("Результат", f"Выбран: {var.get()}")

    tk.Button(window, text="Паказать", command=show_value).pack(pady=10)
