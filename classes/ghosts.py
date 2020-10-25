import pygame, sys
from pygame.locals import *
import random

from .maze import checkRoute
from .pac import WHITE

class Ghost(pygame.sprite.Sprite):
  directions = {'UP': True, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def __init__(self, routeMap):
    super(Ghost, self).__init__()
    self.sprite = pygame.image.load("ghost_sprite.jpg")
    self.rect = self.sprite.get_rect()
    self.rect.center = (400, 340)
    self.routeMap = routeMap
    self.ACELERATION = 1
    self.decisions = 0

  def changeDirection(self): #verifica todas as direções que o fantasma pode seguir e decide randomicamente
    oldDirection = ''
    for i in self.directions:
      if self.directions[i]:
        oldDirection = i
    possibleDirections = []

    if checkRoute(self, 0, -10, self.routeMap, WHITE):
      self.directions[oldDirection] = False
      possibleDirections.append('UP')
    if checkRoute(self, 0, +10, self.routeMap, WHITE):
      self.directions[oldDirection] = False
      possibleDirections.append('DOWN')
    if checkRoute(self, -10, 0, self.routeMap, WHITE):
      self.directions[oldDirection] = False
      possibleDirections.append('LEFT')
    if checkRoute(self, +10, 0, self.routeMap, WHITE):
      self.directions[oldDirection] = False
      possibleDirections.append('RIGHT')

    print(possibleDirections)

    if len(possibleDirections) != 0:
      randomDirection = random.choice(possibleDirections)
      self.directions[randomDirection] = True

  def move(self): #troca a posição do fantasma a cada ciclo
    if self.directions['UP'] and checkRoute(self, 0, -1, self.routeMap, WHITE):
      self.rect.move_ip(0, -(self.ACELERATION))
    if self.directions['DOWN'] and checkRoute(self, 0, +1, self.routeMap, WHITE):
      self.rect.move_ip(0, self.ACELERATION)
    if self.directions['LEFT'] and checkRoute(self, -1, 0, self.routeMap, WHITE):
      self.rect.move_ip(-(self.ACELERATION), 0)
    if self.directions['RIGHT'] and checkRoute(self, +1, 0, self.routeMap, WHITE):
      self.rect.move_ip(self.ACELERATION, 0)

    if checkRoute(self, +1, 0, self.routeMap, WHITE, equal=True) or checkRoute(self, -1, 0, self.routeMap, WHITE, equal=True) or checkRoute(self, 0, +1, self.routeMap, WHITE, equal=True) or checkRoute(self, 0, -1, self.routeMap, WHITE, equal=True):
      self.changeDirection()
      

    

    
    
