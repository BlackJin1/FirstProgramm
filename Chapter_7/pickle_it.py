# Консервация
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle,shelve
print("Консервация списков")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Дядя Ваня", "Бондюэль"]
# Открываем на запись новый файл
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nРасконсервация списков.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nПомещение списков на полку")
s = shelve.open("pickles2")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Дядя Ваня", "Бондюэль"]
s.sync() # Убедиться, что данные щаписаны
print("\nИзвлечение списков из файла-полки:")
print("Торговый марки:", s["brand"])
print("Формы:", s["shape"])
print("Виды овощей:", s["variety"])
s.close()
input("\n\nНажмите Enter, чтобы выйти.")




