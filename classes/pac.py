import pygame, sys
from pygame.locals import *

class Pac(pygame.sprite.Sprite):
  COLOR = (125, 125, 125)
  ACELERATION = 1
  directions = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def __init__(self, routeMap):
    super(Pac, self).__init__()
    self.sprite = pygame.image.load("pac_sprite.jpg")
    self.rect = self.sprite.get_rect()
    self.rect.center = (180, 113)
    self.routeMap = routeMap

  def movement(self, eventKey):
    oldDirection = ''
    if eventKey == K_UP or eventKey == K_DOWN or K_LEFT or K_RIGHT:
      for i in self.directions:
        if self.directions[i]:
          oldDirection = i
      if eventKey == K_UP and self.routeMap[self.rect.center[0], self.rect.center[1]-10] != (255, 255, 255, 255):
        self.directions[oldDirection] = False
        self.directions['UP'] = True
      if eventKey == K_DOWN and self.routeMap[self.rect.center[0], self.rect.center[1]+10] != (255, 255, 255, 255):
        self.directions[oldDirection] = False
        self.directions['DOWN'] = True
      if eventKey == K_LEFT and self.routeMap[self.rect.center[0]-10, self.rect.center[1]] != (255, 255, 255, 255):
        self.directions[oldDirection] = False
        self.directions['LEFT'] = True
      if eventKey == K_RIGHT and self.routeMap[self.rect.center[0]+10, self.rect.center[1]] != (255, 255, 255, 255):
        self.directions[oldDirection] = False
        self.directions['RIGHT'] = True
  
  def stopMove(self):
    for i in self.directions:
        self.directions[i] = False

  def move(self):
    if self.directions['UP'] and self.routeMap[self.rect.center[0], self.rect.center[1]-1] != (255, 255, 255, 255):
      #self.y -= self.ACELERATION
      self.rect.move_ip(0, -(self.ACELERATION))
    if self.directions['DOWN'] and self.routeMap[self.rect.center[0], self.rect.center[1]+1] != (255, 255, 255, 255):
      #self.y += self.ACELERATION
      self.rect.move_ip(0, self.ACELERATION)
    if self.directions['LEFT'] and self.routeMap[self.rect.center[0]-1, self.rect.center[1]] != (255, 255, 255, 255):
      #self.x -= self.ACELERATION
      self.rect.move_ip(-(self.ACELERATION), 0)
    if self.directions['RIGHT'] and self.routeMap[self.rect.center[0]+1, self.rect.center[1]] != (255, 255, 255, 255):
      #self.x += self.ACELERATION
      self.rect.move_ip(self.ACELERATION, 0)
    
    if self.routeMap[self.rect.center[0], self.rect.center[1]] == (255, 255, 255, 255):
      self.stopMove()
    
    if self.rect.right <= 155:
      self.rect.left = 650
    
    if self.rect.left >= 651:
      self.rect.right = 155
