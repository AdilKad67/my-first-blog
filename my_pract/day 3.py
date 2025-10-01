from django.contrib.messages.context_processors import messages
from django.db.models.expressions import result
#from pyexpat.errors import messages


#def get_message():
#    return "hello Metanit.com"


#message = get_message()
#print(messages)


#print(get_message())

#def duble(number):
#    return 2 * number

#def print_person(Имя, Возраст):
#    if age > 120 or age < 1:
#        print("неверный возраст")
#        return
#    print(f"Имя: {Имя} Возраст: {Возраст}")


#print_person("Adil", 22)
#print_person("Alisher", 16)


#def print_person(name, age):
#    if age > 120 or age < 1:
#        print("Invalid age")
#        return
#    print(f"Name: {name}  Age: {age}")


#print_person("Adil", 18)
#print_person("Alisher", 16)

#def say_привет(): print("Привет")
#def say_пока(): print("Пока")

#message = say_привет()
#message()
#message = say_пока()
#message()


#def say_hello(): print("Hello")
#def say_goodbye(): print("Good Bye")

#message = say_hello
#message()
#message = say_goodbye
#message()

#def do_operation(a, b, operation):
#    result = operation(a, b)
#    print(f"result = {result}")

#def sum(a, b): return  a + b
#def multiply(a, b):return a * b

#do_operation(5, 4, sum)
#do_operation(5, 4, multiply)

#def sum(a , b): return a + b
#def subtract(a, b): return a - b
#def multiply(a, b): return a * b


#def select_operation(choice):
#    if choice == 1:
#        return sum
#    elif choice == 2:
#        return subtract
#    else:
#        return multiply


#operation = select_operation(1)
#print(operation(10, 6))

#operation = select_operation(2)
#print(operation(10, 6))

#operation = select_operation(3)
#print(operation(10, 6))


#message = lambda: print("привет")

#message()


#print("дарова")


#square = lambda n: n * n

#print(square(32))
#print(square(5))


#sum = lambda a, b: a + b

#print(sum(150, 150))
#print(sum(180, 120))


#a = 300
#b = 1
#c = a / b
#print(c)


#a = "2"
#b = 3
#c = a + b


#age = 18
#message = "Age: " + str(age)
#print(message)


#name = "Adil"


#def say_hi():
#    print("Hello", name)


#def say_bye():
#    print("Good bye", name)

#say_hi()
#say_bye()


#def say_hi():
#    name = "Adil"
#    surname = "Alisher"
#    print("Good bye", name)

#say_hi()
#say_bye()


#"name = "Adil"


#def say_hi():
#    name = "Alisher"


#def say_bye():
#    print("Good bye", name)


#say_hi()
#say_bye()


#def outer():
#    n = 5

#    def inner():
#        nonlocal n
#        n = 25
#        print(n)

#    inner()
#    print(n)


#outer()


#class person:
#    def say_hello(self):
#        print("Hello")

#tom = person()
#tom.say_hello()


#class Person:

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def display_info(self):
#        print(f"Name: {self.name} Age: {self.age}")


#Adil = Person ("Adil", 18)
#Adil.display_info()

#Alisher = Person ("Alisher", 16)
#Alisher.display_info()


#class person:

#    def __init__(self, name):
#        self.name = name
#        print("Создан человек с именем", self.name)

#    def __del__(self):
#        print("Удален человек с именем", self.name)

#Adil = person("Dexter")


#class person:
#   def __init__(self, name):
#        self.name = name
#        print("Создан человек с именем", self.name)

#    def __del__(self):
#        print("Удален человек с именем", self.name)


#def create_person():
#    adil = person("Adil")

#create_person()
#print("Конец программы")


class person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def set_age

