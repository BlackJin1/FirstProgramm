# Анализатор текста
# Демонстриарует работц функции len() и опреатора in

message = input("Введите текст: ")
print("\nДлинна введенного вами текста состовляет: ", len(message))
print("\nСамая частая согласная. 'т' ")
if 'т' in message:
    print("Встречается в текста.")
else:
    print("Не встречатеся в тексте.")
input("Нажмите Enter, чтобы выйти.")
