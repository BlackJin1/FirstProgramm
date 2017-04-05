# Только согласные
# Демонстрирует, как создавать новые строки из исходной с помощью цикла for

message = input("Введите текст: ")
new_message = ""
VOWELS = "аеiоuаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message +=letter
        print("Создана новыя строка: ", new_message)
print("\nВот ваш текст и изъятыми гласными буквами: ", new_message)
input("\nНадмите Enter, чтобы выйти.")
