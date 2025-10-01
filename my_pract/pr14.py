# import pygame
#
# pygame.init()
# screen_width = 400
# screen_height = 300
# pygame.display.set_mode((screen_width,screen_height))
# screen_color = (0, 0, 255)
# screen_position = (100,150)
# screen_size = 50
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     screen.fill(255,255,255)
#     pygame.draw.rect(screen,screen_color,(screen_position[0]),screen_position[1],screen_size,screen_size)
#     pygame.display.flip()
# pygame.quit()
from os import write

# import pygame
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Квадрат")
#
# BLACK = (0, 0, 0)
# PURPLE = (255, 0, 255)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill(BLACK)
#     pygame.draw.rect(screen, PURPLE, (100, 100, 100, 100))
#     pygame.display.flip()
# pygame.quit()

# import pygame
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Квадраты")
#
# BLACK = (0, 0, 0)
# LIME = (0, 255, 0)
# square_size = 50
# square_color = LIME
# squares = []
# for i in range(12):
#     new_square = pygame.Rect(i * 70 , 50, square_size, square_size)
#     squares.append(new_square)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill(BLACK)
#     for square in squares:
#         pygame.draw.rect(screen, square_color, square)
#     pygame.display.flip()
# pygame.quit()

import pygame
import random

from pygame.sysfont import font_constructor

from my_pract.pr10 import text_rect

pygame.init()
dis=pygame.display.set_mode((800,800))
pygame.display.set_caption("КВАДРАТЫ")
font = pygame.font.SysFont(None,36)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis_over=True
    dis.fill("red")
    counter=1
    for a in range(11):
        for b in range(11):
            x = 20 + b * 70
            y = 20 + a * 70
            r = pygame.Rect(x ,y ,50 , 50)
            color = random.randint(0,255),random.randint(0,255),random.randint(0,120)
            pygame.draw.rect(dis,color,r,width=0)
            text = font.render (str(counter), True, (0,0,0))
            text_rect = text.get_rect(center=r ,center)
            dis.blit

    pygame.display.update()
quit()




