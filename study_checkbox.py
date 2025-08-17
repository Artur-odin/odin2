import tkinter as tk
from tkinter import messagebox

def study_checkbox():
    """Изучение флажков"""
    window = tk.Toplevel()#есди просто Tk, то на других кнопках будут точки
    window.title("Чекбоксы")
    window.geometry("300x200")

    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    
    tk.Label(window, text="Выберите язык:").pack(pady=5)
    tk.Checkbutton(window, text="Python", variable=var1).pack()
    tk.Checkbutton(window, text="Java", variable=var2).pack()
    tk.Checkbutton(window, text="C++", variable=var3).pack()

    def show_choice():
        longs = []
        
        if var1.get():
            longs.append("Python")
        if var2.get():
            longs.append("Java")
        if var3.get():
            longs.append("С++")
        messagebox.showinfo("Результат", f"Выбран: {', '.join(longs)}")

    tk.Button(window, text="Паказать", command=show_choice).pack(pady=10)