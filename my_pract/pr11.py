# class animal:
#         def __init__(self, poroda, cvet, age):
#
#             self.poroda = poroda
#             self.cvet = cvet
#             self.age = age
#             self.miu = False
#
#         def miu(self):
#
#             if not self.miu_on:
#                 self.miu_on = True
#                 print(f"Кот {self.poroda} {self.cvet} начал мяукать.")
#             else:
#                 print("Кот уже мяукает.")
#
#         def stop_miu(self):
#             if self.miu_on:
#                 self.miu_on = False
#                 print(f"Кот {self.poroda} {self.cvet} перестал мяукать.")
#             else:
#                 print("Кот уже перестал мяукать.")
#
#         def describe(self):
#             print(f"Кот: {self.poroda} {self.cvet}, Возраст: {self.age}")
#
# my_cat = animal("Мейн-кун", "Серый", 4)
# another_cat = animal("Бурма", "Бурый", 2)
#
# my_cat.describe()
# my_cat.start_miu()
# my_cat.start_miu()
# my_cat.stop_miu()
#
# another_cat.describe()


# import message
# print(message.hello)
# message.print_message("hello work")

# import os
#
#
# def get_words(filename):
#     with open(filename, encoding="utf8") as file:
#         text = file.read()
#     text = text.replace("\n", " ")
#     text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#     text = text.lower()
#     words = text.split()
#     words.sort()
#     return words
#
#
# def get_words_dict(words):
#     words_dict = dict()
#
#     for word in words:
#         if word in words_dict:
#             words_dict[word] = words_dict[word] + 1
#         else:
#             words_dict[word] = 1
#     return words_dict
#
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename):
#         print("Указанный файл не существует")
#     else:
#         words = get_words(filename)
#         words_dict = get_words_dict(words)
#         print(f"Кол-во слов: {len(words)}")
#         print(f"Кол-во уникальных слов: {len(words_dict)}")
#         print("Все использованные слова:")
#         for word in words_dict:
#             print(word.ljust(20), words_dict[word])
#
# #
# # if __name__ == "__main__":
# #     main()
#    screen_width = 800
#     screen_height = 600
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     roof_points = [(100, 200), (200, 100), (300, 200)]
#
#     roof_color = (255, 0, 0)  # Красный цвет
#     pygame.draw.polygon(screen, roof_color, roof_points)
#
# import pygame
#
# pygame.init()
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# house_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
#
# pygame.draw.rect(house_surface, (139, 69, 19), (0, 50, 200, 150))
# pygame.draw.polygon(house_surface, (165, 42, 42), [(0, 50), (100, 0), (200, 50)])
# pygame.draw.rect(house_surface, (82, 45, 100), (75, 120, 50, 80))
# pygame.draw.rect(house_surface, (0, 255, 255), (30, 80, 40, 40))
#
# screen.blit(house_surface, (100, 100))
# pygame.display.update()
# pygame.quit()

# import pygame
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# WHITE = (255, 255, 255)
# BROWN = (139, 69, 19)
# RED = (165, 42, 42)
# PURPLE = (82, 45, 100)
# CYAN = (0, 255, 255)
# pygame.display.update()
# quit()

# import pygame
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# house_surface = pygame.Surface((200, 250), pygame.SRCALPHA)
#
# wall_color = (200, 150, 100)
# pygame.draw.rect(house_surface, wall_color, (0, 50, 200, 200))
#
# roof_color = (150, 50, 50)
# roof_points = [(50, 0), (150, 0), (100, 100)]
# pygame.draw.polygon(house_surface, roof_color, roof_points)
#
# door_color = (100, 75, 50)
# pygame.draw.rect(house_surface, door_color, (75, 150, 50, 100))
#
# window_color = (100, 200, 255)
# pygame.draw.rect(house_surface, window_color, (120, 75, 50, 50))
#
# running = True
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((135, 206, 235))
#
#     screen.blit(house_surface, (50, 100))
#
#     pygame.display.flip()
#
# pygame.quit()
# from pygame import (init as pg_init, quit as pg_quit, QUIT as ev_quit, K_c as key_c)
# from pygame.display import (set_mode, set_caption as win_title, flip as display_flip)
#
# from pygame.rect import Rect
# from pygame.draw import rect
#
# from pygame.font import init as font_init, SysFont
# from pygame.event import get as pg_ev_get
# from pygame.key import get_pressed
#
# from sys import exit as sys_exit
#
# pg_init()
# font_init()
#
# window = set_mode((800, 800))
#
# win_title('titl')
#
# running = True
#
# font = SysFont('Arial', 16)
#
# x = 30
#
# while running:
#     r_rect = Rect(x, 0, 50, 50)
#     _rect = rect(window, (255, 255, 255), r_rect)
#
#     window.blit(font.render(str(x), True, (255, 255, 255)), (0, 0))
#
#     for event in pg_ev_get():
#         if event.type == ev_quit:
#             pg_quit()
#
#             sys_exit(0)
#
#     keys = get_pressed()
#
#     if keys[key_c]:
#         x += 1
#
#     display_flip()

import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Квадрат")

BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
square_size = 50
square_color = PURPLE
squares = []
for i in range(12):
    new_square = pygame.Rect(i * 70 , 50, square_size, square_size)
    squares.append(new_square)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for square in squares:
        pygame.draw.rect(screen, square_color, square)
    pygame.display.flip()
pygame.quit()

