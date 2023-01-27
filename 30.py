# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


a1 = int(input("Введите первый элемент арифметической прогрессии:  "))
d = int(input("Введите разность арифметической прогрессии:  "))
n = int(input("Введите количество элементов арифметической прогрессии:  "))

list = [a1 + (ni-1) * d  for ni in range(1, n + 1)]
print(*list)