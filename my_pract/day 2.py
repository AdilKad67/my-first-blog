#number = 3

#while number < 7:
 #   print(f"number = {number}")
 #   number += 1
#print("Работа программы завершена")

#print(f"number = {number}")
#number += 6

#p = float(input("250000: "))
#r = float(input("45: "))
#t = float(input("5: "))

#si = (p * r * t) / 100
#print("190000.0: ", si)

#c = float(input("30: "))

#f = (9/5)*c + 32
 # вывод результата
#print(c, " 30 ", f,  " 86 ")

# ввод года
#y = int(input("Введите год: "))

# проверка года
#if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
 #   print("Год високосный")
#else:
 #   print("Год не високосный")

#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))
#if a>b:
#    g=a
#else:
#    g=b
#print("Наибольшее число: ",g)

#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))
#g =  a if a>b else b
#print("Наибольшее число: ",g)

# вводим сумму продажи
#amount = int(input("Введите сумму продажи: "))
# вычисление скидки
#if amount > 0:
 #   if amount>25000:
  #      discount=amount * 0.3
  #  elif amount>15000:
  #      discount=amount * 0.2
  #  elif amount>5000:
  #      discount = amount*0.12
  #  else:
  #      discount = amount*0.05
  #  print("Скидка: ", discount)
  #  print("Сумма с учетом скидки : ", amount-discount)
#else:
 #   print("Некорректная сумма")

# бесконечный цикл
#while True:
 #   # вводим первое число
  #  num1 = int(input("Введите первое число: "))
 #   # вводим второе число
 #   num2 = int(input("Введите второе число: "))
 #   # вычисление суммы чисел
 #   print("Сумма чисел: ", num1+num2 )
 #   # запрос на выход из цикла
 #   str = input ("Нажмите Y или y для завершения программы: ")
    # выходим из цикла
 #   if (str =="Y" or str =="y"):  break

#n = 7
#for i in range(0, n):
 #   for j in range(0, n):
  #      if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
   #     else: print(" ", end="")
   # print()

#h= 7
#w = h + 2
#m = w //4
#for i in range(1, h+1):
 #    if (i <= m):
  #       print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
   #  else:
    #   print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))


#n=5
#k=1
#counter=1
#for i in range(n):
 #   for j in range(n):
  #      if k % 2 == 0:
   #         print(counter, end="  ")
    #        counter+=1
    # 3   else: print("*",end="  ")
      #  k+=1
    #print()

#def say_hello():
 #   print("Hello")


#say_hello()
#say_hello()
#say_hello()

#def say_hello(): print("hi")

#say_hello()

#def say_привет():
#    print("привет")

#def print_messages():
#    def say_hello(): print("hello")
#    def say_goodbye(): print("good bye")

#def main():
 #   say_hello()
 #   say_goodbye()

#def say_hello():
#    print("hello")

#def say_goodbye():
#    print("good bye")

#main()

#def say_привет(name):
#    print(f"привет, {name}")

#say_привет("Adil")
#say_привет("Alisher")
#say_привет("Ravil")

#def print_person(Имя, Возраст):
 #   print(f"Имя: {Имя}")
 #   print(f"Возраст: {Возраст}")


#print_person("Adil", 18)


#def say_hello(name="Adil"):
#    print(f"Hello, {name}")


#say_hello()
#say_hello("Ramil")

#def print_person(name, /, age = 18, *, company):
#    print(f"Name: {name}  Age: {age}  Company: {company}")


#print_person("Adil", company ="Valve")
#print_person("Alisher", 16, company ="Lego" )
#print_person("Ravil", company ="Google", age = 20 )

def sm(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1, 2, 3, 4, 5)
sum(3, 4, 5, 6)


def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1, 2, 3, 4, 5)  # sum = 15
sum(3, 4, 5, 6)  # sum = 18



