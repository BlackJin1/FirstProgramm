# Киноман - 2
# Демонстрирует переключатель
from tkinter import *
class Application(Frame):
    """ GUI-Приложение, позволяющее выбрать только один жанр"""
    def __init__(self, master):
        """ Инициализируем рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает элементы, с помощью которых пользователь будет выбирать """
        # Метка
        Label(self,
              text="Укажите ваш любимый жанр кино.").grid(row=0, column=0, sticky=W)
        # Метка инструкция
        Label(self,
              text="Выберите ровно 1:").grid(row=1, column=0, sticky=W)
        # Переменная для хранения сведений о единственном любимом жанре
        self.favorite = StringVar()
        self.favorite.set(None)

        # Положение Камедия переключателя
        Radiobutton(self,
                    text="Комедия",
                    variable=self.favorite,
                    value="комедия",
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        # Положение Драма переключателя
        Radiobutton(self,
                    text="Драма",
                    variable=self.favorite,
                    value="драма",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        # Положение Кино о любви переключателя
        Radiobutton(self,
                    text="Кино о любви",
                    variable=self.favorite,
                    value="кино о любви",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # Текстовая область с результатами
        self.result_text = Text(self, width=40, height=5, wrap=WORD)
        self.result_text.grid(row=5, column=0, columnspan=3)


    def update_text(self):
        """ Обновляет текстовую область, вписывает в нее любимый жанр """
        message = "Ваш любимый киножанр "
        message += self.favorite.get()
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, message)


# Основной код
root = Tk()
root.title("Киноман - 2")
app = Application(root)
app.mainloop()