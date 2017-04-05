# Считалка
# Демонстрирует испольование функции range()

print("Посчитвем: \n")
for i in range(10):
    print(i, end=" ")

print("\nПеречислим кратные 5:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\nПеречислим в обратном порядке:")
for i in range(10,0,-1):
    print(i,end=" ")

input("\nНажмите Enter, чтобы выйти\n")

