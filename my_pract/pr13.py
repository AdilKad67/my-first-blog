# import pygame
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
import pygame as pg
import sys
from pygame.color import THECOLORS

pg.init()
sc = pg.display.set_mode((800, 500))
pg.display.set_caption("SNOWMAN")
sc.fill((127, 255, 212))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.draw.circle(sc, (250,250,250),(375,400),50)
    pg.draw.circle(sc, (250,250,250),(375,330),30)
    pg.draw.circle(sc, (250,250,250),(375,285),20)
    pg.draw.circle(sc, (0,0,0),(370,280),1)
    pg.draw.circle(sc, (0,0,0),(385,280),1)

    # font = pg.font.Font(None,50)
    # text_surface = font.render("SNOWMAN",True, (255,255,255))
    # text_x = sc
    # text_y = sc // 2 - text_surface.get


    font = pg.font.SysFont('couriernew',40)
    text = font.render(("SNOWMAN"),True, THECOLORS['pink'])
    sc.blit(text, (50, 360))
    text_x = sc


    pg.display.update()


quit()