'''
Задача 4

Пользователь вводит 3 числа, сказать сколько из них положительных
и сколько отрицательных

'''
number_1 = int(input("Введите первое число:"))
number_2 = int(input("Введите второе число:"))
number_3 = int(input("Введите третье число:"))

print("Положительных чисел:", (number_1 > 0) + (number_2 > 0) + (number_3 > 0))
print("Отрицательных чисел:", (number_1 < 0) + (number_2 < 0) + (number_3 < 0))

