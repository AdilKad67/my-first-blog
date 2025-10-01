# name = input("Введите ваше имя:")
# print("привет",name)
# age = print (input("сколько тебе лет"+name+"?"))
from django.db.models.expressions import result

# a =float (input("Введите первое число:"))
# b =float (input("Введите второе число:"))
# m = a + b
# print("ваш ответ:",m)
# n = a * b
# print("Ваш ответ:",n)
# c = a - b
# print("Ваш ответ:",c)
# r = a / b
# print("Ваш ответ:",r)

# p = float(input("Начальная сумма вклада: "))
# r = float(input("Процент по вкладу: "))
# t = float(input("Количество лет: "))
#
# si = (p * r * t) / 100
# print("Начисленные проценты: ", si)

# c = float(input("Введите температуру в градусах цельсия: "))
# f = (9/5)*c + 32
# print(c, " градусов цельсия равны ", f,  " градусам фаренгейта")

# p = float(input("Введите первое число:"))
# v = float(input("Введите второе число:"))
# b = float(input("Введите третье число:"))
# n = (p + v * b)
# print("ВАШ ОТВЕТ!", n)

# a = 10
# b = 6
# result = 10 == 6
# print(result)
# print(a != b)
# print(a > b)
# print(a < b)
#
# bool1 = True
# bool2 =False
# print(bool1 == bool2)

# age = 18
# weight = 64
# result = age > 18 and weight == 64
# print(result)
#
# age = 18
# isMarried = False
# result = age > 17 or isMarried
# print(result)

from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#F12",
                   font=("Times New Roman", 20),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
