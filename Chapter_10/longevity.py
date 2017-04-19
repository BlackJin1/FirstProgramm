# Долгожитель
# Демонстирует текстовое поле, текстовую область и менеджер размещения Grid
from textwrap import wrap
from tkinter import *
class Application(Frame):
    """ GUI - приложение, владеющая секретом долголетия """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает кнопку, текстовое поле и текстовую область """
        self.inst_lbl = Label(self, text="Чтобы узнать секрет долголетия введите пароль.")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.inst_lbl = Label(self, text="Пароль:")
        self.inst_lbl.grid(row=1, column=0, sticky=W)

        # Текстовое поле для ввода пароля
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # Кнопка отправки значения
        self.submit_bttn = Button(self, text="Узнать секрет", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        # создание текстовой области в которую будет ввыеден ответ
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """ В зависимости от введенного пароля отвечать разными сообщениями """
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Чтобы дожить до 100 лет, надо сначала дожить до 99, а потом" \
                      "вести себя очень аккуратно."
        else:
            message = "Вы ввели неправильный пароль, так что я не могу" \
                      "поделиться найной с вами."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

# основная часть
root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
арр = Application(root)
root.mainloop()