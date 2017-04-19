# Это я, метка
# Демонстрирует применение меток
from tkinter import *
# Создание базового окна
root = Tk()
root.title("Это я, метка")
root.geometry("500x100")

# Внутри окна создается рамка, для размещения других элементов
app = Frame(root)
app.grid()

# Создание метки внутри рамки
lbl = Label(app, text="Вот она я!")
lbl.grid()

# Старт событий цикла
root.mainloop()


