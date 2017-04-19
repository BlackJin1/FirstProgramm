# Киноман
# Демонстрием применением флажков
from tkinter import *
class Application(Frame):
    """ GUI - Приложение, позволяющее выбрать любимые жанры кино."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создаем элементы, с помощью которых пользоавтель будет выбирать. """
        # Метка описания
        Label(self, text="Укажите ваши любимые жанры кино").grid(row=0, column=0, sticky=W)
        # Метка инструкция
        Label(self, text="Выберете все, что вам по вкусу:").grid(row=1, column=0, sticky=W)
        # Флажек - Камедия
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text="Комедия",
                    variable=self.likes_comedy,
                    command=self.update_text).grid(row=2, column=0, sticky=W)
        # Флажек - Драма
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text="Драма",
                    variable=self.likes_drama,
                    command=self.update_text).grid(row=3, column=0, sticky=W)
        # Флажек - Фильм о любви
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text="Фильм о любви",
                    variable=self.likes_romance,
                    command=self.update_text).grid(row=4, column=0, sticky=W)

        # Текстовая область с результатами
        self.result_text = Text(self, width=40, height=5, wrap=WORD)
        self.result_text.grid(row=5, column=0, columnspan=3)


    def update_text(self):
        """ Обновляет текстовый элемент, по мере того, как польщователь выбрает свои любимые киножанры. """
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комадии.\n"
        if self.likes_drama.get():
            likes += "Ваc привлекает жанр драмы.\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу кино о любви.\n"
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, likes)


# Основной код
root = Tk()
root.title("Киноман")
app = Application(root)
app.mainloop()