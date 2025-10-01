#name = input("Введите имя: ")
#print("Привет,", name)
#print(2+3)
#print("Hello")
#print(2 + 3)
    #print("Hello")
#if 1 < 2:
 #   print("Hello")
#print("Full name:", "Adil", "Kadyrov")
#name = input("Введите имя: ")
#print("Привет", name)
# две разные переменные
#name = "Adil"
#Name = "Adil"
#name = "Adil"  # определение переменной name
#print(name)   # вывод значения переменной name на консоль
#name = "Adil" # переменной name равна "Adil"
#print(name)   # выводит : Adil
#name = "Alisher" # меняем значение на "Alisher"
#print(name)   # выводит: Alisher
#isMarried = False
#print(isMarried)   # False
#isAlive = True
#print(isAlive)     # True
#age = 18
#print("Возраст:", age)   # Возраст: 18
from email.utils import encode_rfc2231
from tkinter.font import names
from urllib.parse import ParseResult

from sqlparse.utils import offset

#count = 17
#print("Количество:", count)  # Количество: 17
#print(a)  # 7 в десятичной системе
#print(b)  # 9 в десятичной системе
#print(c)  # 15 в десятичной системе
#a = 0o7
#b = 0o11
#c = 0o17
#print(a)
#print(b)
#print(c)
#a = 0x0F
#b = 0xFC
#c = 0xAF
#print(a)
#print(b)
#rint(c)
#eight = 1.22
#i = 3.14
#eight = 56.
#rint(height)  # 1.22
#rint(pi)      # 3.14
#rint(weight)  # 56.0
#x = 3.9e3
#print(x) # 3900.0

#x = 3.9e-3
#print(x) #0.0039
#complexNumber = 1+2j
#print(complexNumber)   # (1+2j)
#message = "Hello World!"
#print(message)  # Hello World!

#name = 'Adil'
#print(name)  # Adil
#text = ("Laudate omnes gentes laudate"
 #       "magnificat in secula")
#print(text)
#'''
#это комментарий
#'''
#text = '''Laudate omnes gentes laudate
#Magnificat in secula
#Et anima mea laudate
#Magnificat on secula
#'''
#print(text)
#text = "Сообщение:\n\"Привет\""
#print(text)
#path = "C:\pack\name.txt"
#print(path)
#userName = "Adil"
#userAge = 18
#user = f"name: {userName}  age: {userAge}"
#print(user)   # name: Adil  age: 18

#userId = "wasd"  # тип str
#print(userId)

#userId = 777  # тип int
#print(userId)
#userId = ("wasd")  # тип str
#print(type(userId)) # <class 'str'>
#userId = 777         # тип int
#print(type(userId))  # <class 'int'>
#print("Hello World", end=" ")
#print("Hello Google.COM", end=" ")
#print("Hello Python")
#name = input("Введите свое имя: ")
#print(f"Ваше имя: {name}")
#name = input("Your name: ")
#age = input("Your age: ")
#print(f"Name: {name} Age: {age}")
#print(5 + 3) # 8
#print(6+9)   # 15
#print(13+17) # 30
#print(2*5)  # 10
#print(5*5)  #25
#print(100/10) # 10
#print(7/2)  #3.5
#print(7//2) # 3
#print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36
#print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1
#number = 3 + 4 * 5 ** 2 + 7
#print(number)  # 110
#number = (3 + 4) * (5 ** 2 + 7)
#print(number)  # 224
#number = 10
#number += 5
#print(number)  # 15

#number -= 3
#print(number)  # 12

#number *= 4
#print(number)  # 48
#first_number = 2.0001
#second_number = 5
#third_number = first_number / second_number
#print(third_number) # 0.40002000000000004
# округление до двух знаков после запятой
#print(round(2.545, 2))  # 2.54
#print(round(2.555, 2))  # 2.56 - округление до четного
#print(round(2.565, 2))  # 2.56
#rint(round(2.575, 2))  # 2.58

#print(round(2.655, 2))  # 2.65 - округление не до четного
#print(round(2.665, 2))  # 2.67
#print(round(2.675, 2))  # 2.67
#a = 7
#b = 8
#result = 7 == 8  # сохраняем результат операции в переменную
#print(result)  # False - 7 не равно 8
#print(a != b)  # True
#print(a > b)  # False - 7 меньше 8
#print(a < b)  # True

#bool1 = True
#bool2 = False
#print(bool1 == bool2)  # False - bool1 не равно bool2

age = 18
weight = 64
result = age > 18 and weight == 64
print(result)  # True
age = 22

isMarried = False
result = age > 18 or isMarried
print(result)  # True, так как выражение age > 18 равно True

result = 4 and "w"
print(result)  # w, так как 4 равно True, поэтому возвращается значение последнего операнда

result = 0 and "w"
print(result)  # 0, так как 0 эквивалентно False

result = 4 or "w"
print(result)

result =