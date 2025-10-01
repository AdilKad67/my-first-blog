#a = float (input("введите 1 число:"))
#b = float (input("введите 2 число:"))
#if a > b:
 #  print("1 число больше чем 2")
#if a < b:
#    print("2 число больше чем 1")
# from tkinter.font import names
#
# name= input("Введите имя:")
# fam = input("Введите фамилию:")
# print("вас зовут:",name , fam)

# for c in range(20):
   # input("Введите вашу фамилию:")

# for n in range(7, 22):
#      print(n, end=" ")

# for n in range(0,50, 2):
#     print(n, end=" ")

# for n in range(50 // 2):
#     print(n, end=" ")

# число = 7

# while число < 23:
#     print(f"число = {число}")
#     число += 1

# n = 10
# while n < 5:
#     print(f"n= {n}")
#     n += 1
# else:
#     print(f"n = {n}. работа завершена")
# print("Работа проги завершена")

# language = "english"
# if language == "english":
#     print("Привет")
# print("End")

# language = "english"
# if language == "english":
#     print("Hello")
# else:
#     print("Привет")
# print("End")
# a = input("Введите 1 число:")
# b = input("Введите 2 число:")
# c = input("Введите 3 число:")
# if a > b and a > c:
#     print(f"Число {a} Наибольшее")
# elif b > a and b > c:
#     print(f"Число {b} Наибольшее")
# else:
#     print(f"Число {c} Наибольшее")
#
# a = input("Введите 1 число:")
# b = input("Введите 2 число:")
# c = input("Введите 3 число:")
# d = input()
#
# print(min(10, 5, 20, 15))
# print(max(10, 5, 20, 15))

a = int(input("Введите число элементов списка:"))
sp = []
for i in range (a):
s = sum(sp)
positive = 0
negative = 0
for num in sp:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print("Список:", sp)
print("Сумма элементов:", s)
if a > 0:
    average = s / a
    print("Среднее арифметическое:", average)
    print("Количество положительных чисел:", positive)
    print("Количество отрицательных:", negative)


