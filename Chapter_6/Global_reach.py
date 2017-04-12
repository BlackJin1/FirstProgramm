# Доступ отовсюду
# Демонстрация работы с глобальными переменными

def read_global():
    print("В области видимости функции read_global() значение value равно: ", value)

def shadow_global():
    value = -10
    print("В области видимости функции shadow_global() значение value равно: ", value)

def change_global():
    global value
    value = -10
    print("В области видимости функции change_global() значение value равно: ", value)

# Основная часть
# value - глобальная переменная, потому что сейчас мы находимся в глобальной области видимости
value = 10
print("В глобальной области видимости значение переменной value стало равным: ", value)
read_global()
print(" Вернемся в глобальную область вилимости, здесь value по-прежнему равно: ", value)
shadow_global()
print("Вернемся в глобальную область вилимости, здесь value по-прежнему равно: ", value)
change_global()
print("Вернемся в глобальную область вилимости, здесь value изменилось на: ", value)
input("Нажмите Enter, чтобы выйти.")