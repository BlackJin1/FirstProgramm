# Случайные буквы
# Демонстрирует индексацию строк
import random
word = "индекс"
print("В переменной word храниться слово ", word, "\n")
high = len(word)
low = - len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t",word[position])
input("Введите Enter, чтобы продолжить.")

