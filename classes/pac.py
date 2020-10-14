import pygame, sys
from pygame.locals import *

class Pac:
  COLOR = (125, 125, 125)
  ACELERATION = 1
  directions = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def __init__(self, x, y, width, heigth):
    self.x = x
    self.y = y
    self.width = width
    self.heigth = heigth

  def get_rect(self):
    return pygame.Rect(self.x, self.y, self.width, self.heigth)

  def drawPac(self, display):
      pygame.draw.rect(display, self.COLOR, [self.x, self.y, self.width, self.heigth])

  def movement(self, eventKey):
    if eventKey == K_UP or eventKey == K_DOWN or K_LEFT or K_RIGHT:
      for i in self.directions:
        self.directions[i] = False
      if eventKey == K_UP:
        self.directions['UP'] = True
      if eventKey == K_DOWN:
        self.directions['DOWN'] = True
      if eventKey == K_LEFT:
        self.directions['LEFT'] = True
      if eventKey == K_RIGHT:
        self.directions['RIGHT'] = True

  def move(self):
    if self.directions['UP']:
      self.y -= self.ACELERATION
    if self.directions['DOWN']:
      self.y += self.ACELERATION
    if self.directions['LEFT']:
      self.x -= self.ACELERATION
    if self.directions['RIGHT']:
      self.x += self.ACELERATION
  
  def stopMove(self):
    for i in self.directions:
        self.directions[i] = False
