nume_1: int = int(input("Введите первое число:"))
sign = input("Введите знак:")
nume_2: int = int(input("Введите второе число:"))

'''
try: nume_1/ nume_2
except: ZeroDivisionError
print("На ноль делить нельзя:")
'''
if sign == "+":
    print(nume_1 + nume_2)
elif sign == "-":
    print(nume_1-nume_2)
elif sign == "*":
    print(nume_1*nume_2)
elif sign == "/":
    print(nume_1/nume_2)
elif nume_2 ==0:
    print("На ноль делить нельзя:")

else:
    print("Неверная операция:")

