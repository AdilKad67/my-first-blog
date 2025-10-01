# class person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Adil = person ("Adil", 18)
# print(Adil.name)
# print(Adil.age)
# Adil.age = 20
# print(Adil.age)



# class person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Adil = person("Adil",18)
# Alisher = person("Alisher",17)
# print(Adil.name)
# # print(Alisher.name)
#
#  student:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
# Adil = student("Adil",32)
# print(Adil.group)
# class

# class Person:
#     def say(self, message):
#         print(message)
#
#
# tom = Person()
# tom.say("Hello METANIT.COM")

# class student:
#
#     def __init__(self, name, group, age):
#         self.name = name
#         self.age = age
#         self.group = group
#
#
# Adil = student("Adil", 32, 18)
# Adil.college = "College IT"
# print("Имя:",Adil.name)
# print("Группа:",Adil.group)
# print("Возраст:",Adil.age)
# print("Учится в:",Adil.college)
#
#
# Alisher = student("Alisher", 11, 17)
# Alisher.college = "Bussines College"
# print("Имя:",Alisher.name)
# print("Группа:",Alisher.group)
# print("Возраст:",Alisher.age)
# print("Учится в:",Alisher.college)

# class = car:
#     def __init__(self, make, model, year, color):
#     Args:
#         make (str): the brand of the car.
#         model (str): the model of the car.
#         year (str): the year of the car.
#         color (str): the color of the car.
#     self.make = make
#     self.model = model
#     self.year = year
#     self.color = color
#     self.is_running =
# False
#     def start_engine(self):
#         if self.is_running:
#             return f"The {self.make} {self.model} s engine is already running."
#         else:
#             self.is_running =
# True
#             return f"The {self.make} {self.model} s engine has started. Vroom!"

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom", 39)
# tom.__name = "Человек-паук"
# tom.__age = -129
# tom.print_person()

# class animal:
#     def __init__(self, poroda, cvet, age):
#
#         self.poroda =
#         self.model = model
#         self.year = year
#         self.is_engine_on = False
#
#     def start_engine(self):
#
#         if not self.is_engine_on:
#             self.is_engine_on = True
#             print(f"Двигатель автомобиля {self.brand} {self.model} запущен.")
#         else:
#             print("Двигатель уже запущен.")
#
#     def stop_engine(self):
#         if self.is_engine_on:
#             self.is_engine_on = False
#             print(f"Двигатель автомобиля {self.brand} {self.model} остановлен.")
#         else:
#             print("Двигатель уже остановлен.")
#
#     def describe(self):
#         print(f"Автомобиль: {self.brand} {self.model}, год выпуска: {self.year}")
#
# my_car = Car("Volkswagen", "Passat", 2007)
# another_car = Car("BMW", "M5 F90 COMPETITION", 2024)
#
# my_car.describe()
# my_car.start_engine()
# my_car.start_engine()
# my_car.stop_engine()
#
# another_car.describe()

# class student:
#     def __init__(self, name, age, college, group):
#         self.__name = name
#         self.__age = age
#         self.__college = college
#         self.__group = group
#
#     def print_student(self):
#         print(f"Имя:{self.__name}\tВозраст:{self.__age}  Колледж:{self.__college}   Группа:{self.__group}")
# adil = student("Adil",18,"college IT","ВТ32")
# adil.__name = "Школьник"
# adil.__age = -50
# adil.__college = "Бизнес колледж"
# adil.__group = "44"
# adil.print_student()

# class employee:
#     def work(self):
#         print("employee works")
#
# class student:
#     def study(self):
#         print("student studies")
#
# class workingstudent(employee,student):
#     pass
# adil = workingstudent()
# adil.work()
# adil.study()

# class Employee:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# class Student:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def study(self):
#         print(f"{self.name} studies")
#
#
# class WorkingStudent(Employee, Student):
#     pass
#
#
# Adil = WorkingStudent("Adil")
# Adil.work()
# Adil.study()

# class person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#     def display_info(self):
#         print(f"Name: {self.__name} ")
#
# class employee(person):
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# class person:
#     def __init__(self, name):
#     @property
#     def name(self):
#         return self.__name
#     def display_info(self):
#         print(f"Name: {self.__name}")
#
# class employee(person):
#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company
#     def display_info(self):
#         super().display_info()
#         print(f"Company: {self.company}")
#     def work(self):
#         print(f"{self.name}")
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} сказал {sound}"
#
#
# my_cat = Cat("Каспер", 5)
# print(my_cat.description())
# print(my_cat.speak("Мяу"))

import pygame
import random

from pr11 import square

pygame.init()
dis = pygame.display.set_mode((800, 800))
squares = []
square_size = 50
for row in range(10):
    for col in range(10):
        x = col * square_size
        y = row * square_size
        squares.append(pygame.Rect(x, y, square_size, square_size))
font = pygame.font.Font(None, 40)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dis.fill((0, 255, 0))
    for i, rect in enumerate(squares):
        for a in range(11):
            for b in range(11):
             = 20 + b * 70
            y = 20 + a * 70
            r = pygame.Rect(x ,y ,50 , 50)
            color = random.randint(0,255),random.randint(0,255),random.randint(0,120)
            pygame.draw.rect(dis,color,r,width=0)
        # pygame.draw.rect(screen, (255, 255, 0), rect)
        text_surface = font.render(str(i + 1), True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        dis.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()
