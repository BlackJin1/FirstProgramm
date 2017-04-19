# Бесполезные кнопки
# Демонстрирует создание кнопок
from tkinter import *
# Создание базового окна
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("200x85")
# Внутри окна создаем рамку для размещения других элементов
app = Frame(root)
app.grid()
# Создание кнопок внутри рамки
btn1 = Button(app, text="Я ничего не делаю!")
btn1.grid()

btn2 = Button(app)
btn2.grid()
btn2.configure(text="И я тоже!")

btn3 = Button(app)
btn3.grid()
btn3["text"] = "И я!"

# Старт событийного цикла
root.mainloop()
