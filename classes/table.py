import pygame, sys
from pygame.locals import *

class TableRect:
  rectColor = (255,255,255)

  def __init__(self, x, y, width, heigth):
    self.x = x
    self.y = y
    self.width = width
    self.heigth = heigth

  def get_rect(self):
    return pygame.Rect(self.x, self.y, self.width, self.heigth)

  def drawTable(self, display):
      pygame.draw.rect(display, self.rectColor, [self.x, self.y, self.width, self.heigth])

weigth = 3
POSITIONS = [
  (100, 125, 285, weigth),
  (400, 125, 285, weigth),
  (685, 128, weigth, 135),
  (560, 263, 125, weigth),
  (557, 266, weigth, 25),
  (560, 291, 125, weigth),
  (560, 326, 125, weigth),
  (557, 329, weigth, 25),
  (560, 354, 125, weigth),
  (97, 128, weigth, 135),
  (100, 263, 125, weigth),
  (225, 266, weigth, 25),
  (100, 291, 125, weigth),
  (100, 326, 125, weigth),
  (225, 329, weigth, 25),
  (100, 354, 125, weigth),
  (685, 357, weigth, 70),
  (97, 357, weigth, 70),
  (100, 427, 45, weigth),
  (145, 430, weigth, 9),
  (100, 439, 45, weigth),
  (97, 442, weigth, 70),
  (100, 512, 585, weigth),
  (640, 427, 45, weigth),
  (637, 430, weigth, 9),
  (640, 439, 45, weigth),
  (685, 442, weigth, 70),
  (385, 128, weigth, 45),
  (397, 128, weigth, 45),
  (388, 173, 9, weigth)
]


'''

RETANGULO = pygame.Rect(100, 110, 50, 50)
pygame.draw.rect(window, (125,125,125), [100,110,50,50])
print(RETANGULO.collidelist(tableCollideList))

'''