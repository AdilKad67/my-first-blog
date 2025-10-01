from platform import uname

# a = int(input("Введите число элементов списка:"))
# sp = []
# s = 0
# for i in range (1, a+1):
#     sp.insert(i,int(input(f"Введите {i} число: ")))
#     s=s+sp[i]
#     print(s)
# print(sp)
# print(s)
# print(sp[0:a+1])

# a = int(input("Введите число элементов списка:"))
# sp = []
# for i in range (a):
#     num = int(input(f"Введите {i+1} число: "))
#     sp.append(num)
# s = sum(sp)
# print("Список:", sp)
# print("Сумма элементов:",s)
# if a > 0:
#     c = s / a
#     print("Среднее арифметическое элементов:", c)

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








