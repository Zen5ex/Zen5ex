import tkinter as tk

# Функция для обновления поля ввода
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Функция для вычисления результата
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'Ошибка')

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")

# Поле для ввода
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Кнопки для цифр
buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3),
    ('0', 4, 2),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Кнопки операций
operation_buttons = [
    ('+', 4, 1), ('-', 5, 1), ('*', 5, 2), ('/', 5, 3), ('=', 4, 3)
]

for (text, row, col) in operation_buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=39, pady=20, command=evaluate)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Запуск главного цикла
root.mainloop()
