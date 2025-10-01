# from idlelib.iomenu import encoding
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f"{self.name}-у {self.age} года "
#
#     def speak(self, sound):
#         return f"{self.name} сказал {sound}"
#
# from Cat import Cat
#
# with open(hello.txt, 'a', encoding= 'utf-8') as f:
#     f.write(f"{self.name}" says: )
#
from io import text_encoding
from tkinter.font import ITALIC

# import pygame
# from pygame import Surface
# from pygame.display import update
#
# pygame.init()
# adi=pygame.display.set_mode((840,650))
# adi_over=False
# while not adi_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print(event)
#
#     r = pygame.Rect(50, 200, 750, 500)
#     color=(255, 255,0 )
#     pygame.draw.rect(adi,color,r,0)
#
#     r = pygame.Rect(520, 280, 100, 80)
#     color2 = (0, 206, 209)
#     pygame.draw.rect(adi, color2, r, 0)
#
#     r = pygame.Rect(340, 500, 100, 150)
#     color3 = (255, 69, 0)
#     pygame.draw.rect(adi, color3, r, 0)
#
#     r = pygame.Rect(350, 560, 10, 15)
#     color4 = (139, 69, 19)
#     pygame.draw.rect(adi, color4, r, 0)
#
#     roof_color = (150, 50, 50)
#     roof_points = [(50, 0), (150, 0), (100, 0)]
#     pygame.draw.polygon(house_surface, roof_color, roof_points)
#
#
# quit()
#
#
#
#
# import pygame as pg
#
# import sys
#
#
# sc = pg.display.set_mode((300, 700))
#
# sc.fill((0,0,0))
#
# pg.draw.circle(sc, (250,250,250),(150,100),50)
#
# pg.draw.circle(sc, (250,250,250),(150,50),30)
#
# pg.draw.circle(sc, (250,250,250),(150,20),20)
#
# pg.display.update()
#
#
# while 1:
#
# for i in pg.event.get():
#
# if i.type == pg.QUIT:
#
# sys.exit()

# import pygame
# from pygame.examples.scrap_clipboard import screen
#
# pygame.init()
# screen_width = 1000
# screen_height = 900
# screen.fill((127, 255, 212))
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Бегущий текст")
#
# font = pygame.font.Font(None, 36)
# text_surface = font.render("SNOWMAN", True, (35, 55, 25))
# text_rect = text_surface.get_rect()
# text_rect.x = 0
# text_rect.y = screen_height // 2
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     text_rect.x += 1
#     if text_rect.left > screen_width:
#         text_rect.right = 0
# pygame.quit()
#!usr/bin/python3
# import pygame
# import random
#
# WIDTH = 540
# HEIGHT = 740
# FPS = 2
# SIZE_BLOCK = 20
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (224, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Ping Pong")
# clock = pygame.time.Clock()
#
#
# class Snake(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((SIZE_BLOCK, SIZE_BLOCK))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.center = [WIDTH/2, HEIGHT/2]
#         self.speedx = 20
#         self.speedy = 0
#
#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#
#     def tail(self, size_block, snake_list):
#         for x in snake_list:
#             pygame.draw.rect(screen, GREEN, [x[0], x[1], size_block, size_block])
#
#
# class Apple(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((SIZE_BLOCK, SIZE_BLOCK))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.foodx = round(random.randrange(0, WIDTH - SIZE_BLOCK) / 20.0) * 20.0
#         self.foody = round(random.randrange(0, HEIGHT - SIZE_BLOCK) / 20.0) * 20.0
#
#     def update(self):
#         self.rect.x = self.foodx
#         self.rect.y = self.foody
#
#
# all_sprites = pygame.sprite.Group()
# apples = pygame.sprite.Group()
# apple = Apple()
# snake = Snake()
# all_sprites.add(snake)
# all_sprites.add(apple)
# apples.add(apple)
#
#
# snake_list = []
# len_of_snake = 1
# running = True
# while running:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a and snake.speedy != 0:
#                 snake.speedx = -SIZE_BLOCK
#                 snake.speedy = 0
#             if event.key == pygame.K_d and snake.speedy != 0:
#                 snake.speedx = SIZE_BLOCK
#                 snake.speedy = 0
#             if event.key == pygame.K_w and snake.speedx != 0:
#                 snake.speedx = 0
#                 snake.speedy = -SIZE_BLOCK
#             if event.key == pygame.K_s and snake.speedx != 0:
#                 snake.speedx = 0
#                 snake.speedy = SIZE_BLOCK
#
#     screen.fill(BLACK)
#     all_sprites.draw(screen)
#     if snake.rect.left < -10:
#         running = False
#     if snake.rect.right > WIDTH + 10:
#         running = False
#     if snake.rect.top <= -10:
#         running = False
#     if snake.rect.bottom > HEIGHT + 10:
#         running = False
#
#     snake_head = [snake.rect.x, snake.rect.y]
#     snake_list.append(snake_head)
#     if len(snake_list) > len_of_snake:
#         del snake_list[0]
#
#     for x in snake_list[:-1]:
#         if x == snake_head:
#             running = False
#
#     collide = pygame.sprite.spritecollide(snake, apples, True)
#     if collide:
#         snake.tail(SIZE_BLOCK, snake_list)
#         apple = Apple()
#         all_sprites.add(apple)
#         apples.add(apple)
#         len_of_snake += 1
#         pygame.display.update()
#
#     pygame.display.flip()
#     snake.update()
#     apple.update()
#
# pygame.quit()
#
#
#
# import pygame
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Олимпийские кольца")
#
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)
# GREEN = (0, 255, 0)
#
# radius = 80
# line_width = 10
# circle_x_spacing = 120
# circle_y_spacing = 0
#
# top_blue_center = (screen_width // 2 - 2 * circle_x_spacing, screen_height // 2 - 100)
# top_black_center = (screen_width // 2 - circle_x_spacing, screen_height // 2 - 100)
# top_red_center = (screen_width // 2 + circle_x_spacing, screen_height // 2 - 100)
#
# bottom_yellow_center = (screen_width // 2 - circle_x_spacing // 2, screen_height // 2 + 100)
# bottom_green_center = (screen_width // 2 + circle_x_spacing // 2, screen_height // 2 + 100)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((255, 255, 255))

    # pygame.draw.circle(screen, BLACK, top_black_center, radius, line_width)
    # pygame.draw.circle(screen, BLUE, top_blue_center, radius, line_width)
    #
    # pygame.draw.circle(screen, RED, top_red_center, radius, line_width)
    # pygame.draw.circle(screen, YELLOW, bottom_yellow_center, radius, line_width)
    # pygame.draw.circle(screen, GREEN, bottom_green_center,radius,line_width)
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
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
    screen.fill((0, 255, 0))
    for i, rect in enumerate(squares):
        pygame.draw.rect(screen, (255, 255, 0), rect)
        text_surface = font.render(str(i + 1), True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()

# import pygame
# import random
# pygame.init()
# dis=pygame.display.set_mode((800,800))
# pygame.display.set_caption("КВАДРАТЫ")
#
# dis_over = False
# while not dis_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             dis_over=True
#     dis.fill("red")
#     for a in range(11):
#         for b in range(11):
#             x = 20 + b * 70
#             y = 20 + a * 70
#             r = pygame.Rect(x ,y ,50 , 50)
#             color = random.randint(0,255),random.randint(0,255),random.randint(0,120)
#             pygame.draw.rect(dis,color,r,width=0)
#         for z in range(11):
#             for v in range(11):
#                 x = 20 + b * 70
#                 y = 20 + b * 70
#                 r = pygame.Rect(x , y , 50 , 50)
#
#     pygame.display.update()
# quit()