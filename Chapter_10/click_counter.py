# Счетчик щелчков
# Демонстрирует связываение событий с обработчиками
from tkinter import *
class Application(Frame):
    def __init__(self, master):
        """ Инициализируем рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # количество нажатий
        self.create_widget()

    def create_widget(self):
        """ Создает кнопку, на которой отображается количество нажатий """
        self.bttn = Button(self)
        self.bttn["text"] = "Количество щелчков : 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Увеличение количества нажатий на единицу и отображение его."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество нажатий : "+ str(self.bttn_clicks)

# Основная часть программы
root = Tk()
root.title("Количество щелчков")
root.geometry("200x50")
app = Application(root)
root.mainloop()

