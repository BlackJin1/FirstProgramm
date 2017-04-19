# Бесполезные кнопки -2
# Демонстрирует создание класса в оконном приложениее на основе tkinter
from tkinter import *
class Application(Frame):
    """ GUI- приложение с тремя кнопками"""
    def __init__(self, master):
        """ Инициализируем кнопку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgerts()
    def create_widgerts(self):
        """ Создает три бесполезные кнопки """
        # Создание кнопок внутри рамки
        self.btn1 = Button(self, text="Я ничего не делаю!")
        self.btn1.grid()
        # Ворая кнопка
        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text="И я тоже!")
        # Третья кнопка
        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3["text"] = "И я!"

# Основная часть программы
root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("200x85")

app = Application(root)
root.mainloop()
