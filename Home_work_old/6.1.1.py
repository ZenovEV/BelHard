#Вывести первые N цисел кратные M и больше K

num_1 = int(input("Введите число N:"))
num_2 = int(input("Введите число M:"))
#num_3: int=input("Введите число K:")

for i in range(0, num_2):
    if(i % num_2 == 0):
        print(f"Число {num_1} кратно {num_2}")
else:
    print(f"Число {num_1} некратно {num_2}")


