# Сумасшедший сказочник
# Создает рассказ на основе пользовательского выбора
from tkinter import *
class Application(Frame):
    """ GUI - приложение, создающее рассказ на основе пользовательского выбора """
    def __init__(self, master):
        """ Инициализируем рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает элементы управления, с помощью которых пользователь будет вводить исходные данные и получать 
        готовый заказ"""
        # Метка с текстом инструкции
        Label(self,
              text="Введите данные для создания нового заказа"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        # Метка и поле ввода для имени человека
        Label(self,
              text="Имя человека: ",
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)
        # Метка - поле ввода для существительного
        Label(self,
              text="Существительное во мн. ч.:",
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)
        # Метка поле ввода глагола
        Label(self,
              text="Глагол в инфинитиве: "
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)
        # метка при группе флажков с прилагательным
        Label(self,
              text="Прилагательное (-ые):"
              ).grid(row=4, column=0, sticky=W)
        # Флажок со словом нетерпеливый
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text="нетерпеливый",
                    variable=self.is_itchy,
                    ).grid(row=4, column=1, sticky=W)
        # Флажок со словом радостный
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="радостный",
                    variable=self.is_joyous,
                    ).grid(row=4, column=2, sticky=W)
        # Флажок со словом пронизывающий
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="пронизывающий",
                    variable=self.is_electric,
                    ).grid(row=4, column=3, sticky=W)
        # Метка при переключателе с названиями частей тела
        Label(self,
              text="Части тела: "
              ).grid(row=5, column=0, sticky=W)
        # Переменная, содержащщая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)
        # Переключатель с надваниями частей тела
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part
                        ).grid(row=5, column=column, sticky=W)
            column += 1
        # Кнопка отсылки данных
        Button(self,
               text="Получить рассказ",
               command=self.tell_story
               ).grid(row=6, column=0, sticky=W)
        self.story_text = Text(self, width=75, height=10, wrap=WORD)
        self.story_text.grid(row=7, column=0, columnspan=4)


    def tell_story(self):
        """ Заполняет текстовую область очередной историей на основании пользовательского ввода """
        # Получает значение переменных
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjecktives = ""
        if self.is_itchy.get():
            adjecktives += " нетерпеливое, "
        if self.is_joyous.get():
            adjecktives += " радостное, "
        if self.is_electric.get():
            adjecktives += " пронизывающее, "
        body_part = self.body_part.get()
        # Создание рассказа
        story = "Знаменитый путешественник "
        story += person
        story += " уже совсем отчаялся доверщить дело своей жизни - поиск затерянного города, в котором по " \
                 "легенде, обитали "
        story += noun.title()
        story += ". Но однажды "
        story += noun
        story += " и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное, "
        story += adjecktives
        story += "ни с чем не сравнимое чувство охватило душу путешественниека. "
        story += "После стольких лет поиска цель была наконец достигнута. "
        story += person
        story += " ощутил, как на его " + body_part + " скатилась слезинка. "
        story += "И тут внезапно "
        story += noun
        story += " перешли в атаку, и "
        story += person + " был ими мгновенно сожран."
        story += "Мораль? Если задумали "
        story += verb
        story += ". Надо делать это с осторожностью."
        # Вывод рассказа на экран
        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)




# Основной код
root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
app.mainloop()