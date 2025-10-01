# correct = "111"
# password = input("Введите пароль:")
# while password != correct:
#     print("Неправильный пароль. введите пароль заново:")
#     password = input()
# print("Правильный пароль")
from random import random, randint

# s1 = int(input())
# for i in range(s1):
#     print(i+1,end="\t")
#     for g in range(i):
#         print((g+1)*i)
#         break

# for n in range(1,10):
#     result = 4*n
#     print("4 *",n,"=",result)


# N = int(input("Введите число N:"))
# s = 0
#
# for i in range(N + 1):
#     s += i
# print(f"Сумма чисел от 0 до {N} равна: {s}")

# number = randint(1, 100)
# print("ОТГАДАЙТЕ ЧИСЛО ОТ 1 ДО 100")
# a = 0
# b = 0
# while a != number:
#     b += 1
#     a = int(input(f"{b} - попытка:"))
#     if a > number:
#         print("МНОГО!")
#     elif a < number:
#         print("МАЛО!")
#     else:
#         print(f"ПРАВИЛЬНО, Я ЗАГАДАЛ {number}")

#
a = int(input("Введите число элементов списка:"))
sp = []
for i in range (a):
    num = int(input(f"Введите {i+1} число: "))
    sp.append(num)
s = sum(sp)

if a > 0:
    c = s / a
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












