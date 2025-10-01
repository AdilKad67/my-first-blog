# a = int(input("Введите число элементов списка:"))
# sp = []
# s = 0
# for i in range (a):
#     num = int(input(f"Введите {i+1} число: "))
#     sp.append(num)
#     s = sp
# print("Список:",sp)
# print(f"Сумма элементов списка:", s)
from sqlparse import split

#a = int(input("Введите число:"))
# total = 0
# count = 0
# while True:
#     b=int(input("Введите число(Или введите 0 чтобы завершить программу):"))
#     if b==0:
#        break
#     total += b
#     count += 1
#     print("Кол-во набранных чисел:" ,count)

# a = int(input("Введите число:"))
# number_str = int(input("Введите число:"))
# num = int(number_str)
# a = num // 1000
# f = num % 1000
# b = f // 100
# n = num % 100
# c = n // 10
# x = num % 10
# v = x // 1
# print(f"В числе:{num}")
# print(f"Тысяч:{a}")
# print(f"Сотен:{b}")
# print(f"Десятков:{c}")
# print(f"Единиц:{x}")
#
#  with open("hello.txt", "w") as myfile:
#      print("Работа с файлом myfile")
#

# Программа подсчета слов в файле
import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()








