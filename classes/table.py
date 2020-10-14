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

POSITIONS = [
  (100, 125, 285, 3),
  (400, 125, 285, 3)
]


'''

RETANGULO = pygame.Rect(100, 110, 50, 50)
pygame.draw.rect(window, (125,125,125), [100,110,50,50])
print(RETANGULO.collidelist(tableCollideList))

'''