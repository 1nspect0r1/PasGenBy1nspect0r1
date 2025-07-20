# программа на языке python
# пароль использует модуль(библиотеку Tkinter)
import random
import pyperclip  # Раскомментировал импорт
from tkinter import *
from tkinter.ttk import *

# Функция вычисления пароля
def low():
    entry.delete(0, END)

    # Выбрать длину пароля
    length = var1.get()

    lower = "abcdefghijklmnopqrtuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = ""

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")


# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)


# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
    # Можно добавить подтверждение копирования
    entry.clipboard_clear()
    entry.clipboard_append(random_password)
    entry.update()  # Теперь текст будет в буфере обмена даже после закрытия программы


# Main Function

# create GUI window
root = Tk()

# Убедитесь, что файл favicon.ico существует в той же папке
# root.iconbitmap("favicon.ico")  # Можно раскомментировать, если есть иконка

var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Генератор случайных паролей")
root.resizable(width=False, height=False)

# create label and entry to show
# password generated
Random_password = Label(root, text="Пароль")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# create label for length of password
c_label = Label(root, text="Длина пароля")
c_label.grid(row=1)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Скопировать", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Создать", command=generate)
generate_button.grid(row=0, column=3)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Слабый", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky="E")
radio_middle = Radiobutton(root, text="Средний", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky="E")
radio_strong = Radiobutton(root, text="Сложный", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky="E")
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo["value"] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20, 21, 22, 23, 24, 25,
                  26, 27, 28, 29, 30, 31, 32, 33, 34,
                  35, 36, 37, 38, 39, 40, 50, 51, 52,
                  53, 54, 55, 56, 57, 58, 59, 60, 61,
                  62, 63, 64, "select")
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(column=1, row=1)

# start the GUI
root.mainloop()