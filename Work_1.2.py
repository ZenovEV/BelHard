'''
Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
способами

2-й способ
'''
world = input("Введите текст:")
world = "-".join(world.split())
print(world)