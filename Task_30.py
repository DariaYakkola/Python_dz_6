# Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n)
# нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# from random import randint
a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
array = []
count = 1
while count <= n:
    for i in range(n):
        array.append(a1 + (count - 1) * d)
        count += 1
print(array)
