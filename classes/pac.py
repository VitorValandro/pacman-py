import pygame, sys
from pygame.locals import *
from .maze import checkRoute

WHITE = (255, 255, 255, 255)
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

  def movement(self, eventKey): #função pra mudar a direção do personagem
    oldDirection = ''
    if eventKey == K_UP or eventKey == K_DOWN or K_LEFT or K_RIGHT:
      for i in self.directions:
        if self.directions[i]:
          oldDirection = i
      if eventKey == K_UP and checkRoute(self, 0, -10, self.routeMap, WHITE): #checa se há rota para o personagem
        self.directions[oldDirection] = False
        self.directions['UP'] = True
      if eventKey == K_DOWN and checkRoute(self, 0, +10, self.routeMap, WHITE):
        self.directions[oldDirection] = False
        self.directions['DOWN'] = True
      if eventKey == K_LEFT and checkRoute(self, -10, 0, self.routeMap, WHITE):
        self.directions[oldDirection] = False
        self.directions['LEFT'] = True
      if eventKey == K_RIGHT and checkRoute(self, +10, 0, self.routeMap, WHITE):
        self.directions[oldDirection] = False
        self.directions['RIGHT'] = True
  
  def stopMove(self): #para o movimento do personagem
    for i in self.directions:
        self.directions[i] = False

  def move(self): #função que muda a posição do personagem a cada ciclo
    if self.directions['UP'] and checkRoute(self, 0, -1, self.routeMap, WHITE):
      self.rect.move_ip(0, -(self.ACELERATION))
    if self.directions['DOWN'] and checkRoute(self, 0, +1, self.routeMap, WHITE):
      self.rect.move_ip(0, self.ACELERATION)
    if self.directions['LEFT'] and checkRoute(self, -1, 0, self.routeMap, WHITE):
      self.rect.move_ip(-(self.ACELERATION), 0)
    if self.directions['RIGHT'] and checkRoute(self, +1, 0, self.routeMap, WHITE):
      self.rect.move_ip(self.ACELERATION, 0)
    
    if self.routeMap[self.rect.center[0], self.rect.center[1]] == (255, 255, 255, 255):
      self.stopMove()
    
    if self.rect.right <= 155: #teletransporte do pacman
      self.rect.left = 650
    
    if self.rect.left >= 651:
      self.rect.right = 155
