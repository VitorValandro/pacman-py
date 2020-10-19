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
  #table edge
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
  (388, 173, 9, weigth),
  #top squares
  (135, 163, weigth, 65), (138, 160, 30, weigth), (168, 163, weigth, 65), (138, 228, 30, weigth),
  (206, 163, weigth, 65), (209, 160, 30, weigth), (239, 163, weigth, 65), (209, 228, 30, weigth),
  (277, 163, weigth, 65), (280, 160, 30, weigth), (310, 163, weigth, 65), (280, 228, 30, weigth),
  (469, 163, weigth, 65), (472, 160, 30, weigth), (502, 163, weigth, 65), (472, 228, 30, weigth),
  (543, 163, weigth, 65), (546, 160, 30, weigth), (576, 163, weigth, 65), (546, 228, 30, weigth),
  (614, 163, weigth, 65), (617, 160, 30, weigth), (647, 163, weigth, 65), (617, 228, 30, weigth),
  #phantom spawn
  (355, 280, 20, weigth), (410, 280, 20, weigth), (355, 323, 75, weigth), (352, 283, weigth, 40), (430, 283, weigth, 40),
  (348, 160, weigth, 85), (351, 211, 24, weigth), (432, 160, weigth, 85), (408, 211, 26, weigth),
  
]
