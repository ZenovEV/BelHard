'''
Задача 4

Пользователь вводит 3 числа, сказать сколько из них положительных
и сколько отрицательных
'''
number_1 = int(input("Введите первое число:"))
number_2 = int(input("Введите второе число:"))
number_3 = int(input("Введите третье число:"))

list = [number_1, number_2, number_3]

itog = len([num for num in list if num >= 0])
print(itog)
