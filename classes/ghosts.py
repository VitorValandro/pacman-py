import pygame, sys
from pygame.locals import *
import random

from .maze import checkRoute

WHITE = (255, 255, 255, 255)
spritesheets = ["ghost_sprite.jpg", "ghost_sprite1.jpg", "ghost_sprite3.jpg", "ghost_sprite3.jpg"]

class Ghost(pygame.sprite.Sprite):
  VELOCITY = 1
  def __init__(self, routeMap, spritesheet):
    super().__init__()
    self.sprite = pygame.image.load(spritesheet)
    self.rect = self.sprite.get_rect()
    self.rect.center = (399, 338)
    self.routeMap = routeMap
    self.changePosition = True
    self.directions = {'UP': True, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def verifyChangePosition(self):
    if self.changePosition == True:
      self.changePosition = False
    else:
      self.changePosition = True

  def direcoesPossiveis(self, oldDirection='', directionArray=''):
    possibleDirections = []
    if checkRoute(self, 0, -10, self.routeMap, WHITE):
      if oldDirection != '': directionArray[oldDirection] = False
      possibleDirections.append('UP')
    if checkRoute(self, 0, +10, self.routeMap, WHITE):
      if oldDirection != '': directionArray[oldDirection] = False
      possibleDirections.append('DOWN')
    if checkRoute(self, -10, 0, self.routeMap, WHITE):
      if oldDirection != '': directionArray[oldDirection] = False
      possibleDirections.append('LEFT')
    if checkRoute(self, +10, 0, self.routeMap, WHITE):
      if oldDirection != '': directionArray[oldDirection] = False
      possibleDirections.append('RIGHT')
    
    return possibleDirections

  def changeDirection(self): #verifica todas as direções que o fantasma pode seguir e decide randomicamente
    oldDirection = ''
    for i in self.directions:
      if self.directions[i]:
        oldDirection = i
    possibleDirections = self.direcoesPossiveis(oldDirection=oldDirection, directionArray=self.directions)

    if len(possibleDirections):
      randomDirection = random.choice(possibleDirections)
      if randomDirection == oldDirection and len(possibleDirections) >= 3:
        randomDirection = random.choice(possibleDirections)
      self.directions[randomDirection] = True

  def move(self): #troca a posição do fantasma a cada ciclo
    for i in self.directions:
      if self.directions[i]:
        oldDirection = i
    if self.directions['UP'] and checkRoute(self, 0, -1, self.routeMap, WHITE):
      self.rect.move_ip(0, -(self.VELOCITY))
    if self.directions['DOWN'] and checkRoute(self, 0, +1, self.routeMap, WHITE):
      self.rect.move_ip(0, self.VELOCITY)
    if self.directions['LEFT'] and checkRoute(self, -1, 0, self.routeMap, WHITE):
      self.rect.move_ip(-(self.VELOCITY), 0)
    if self.directions['RIGHT'] and checkRoute(self, +1, 0, self.routeMap, WHITE):
      self.rect.move_ip(self.VELOCITY, 0)
    
    if len(self.direcoesPossiveis()) >= 2 and not oldDirection in self.direcoesPossiveis():
      if self.changePosition == True:
        self.changeDirection()
        self.changePosition = False
      
    elif len(self.direcoesPossiveis()) >= 3:
        self.changeDirection()

    if self.rect.right <= 155:  # teletransporte do fantasma
      self.rect.left = 650

    if self.rect.left >= 651:
      self.rect.right = 155
    
    if self.rect.center == (399, 341): # verifica se ele está no ponto de início
      for i in self.directions:
        self.directions[i] = False
      self.directions['UP'] = True

  def die(self):
    self.rect.center = (399, 338)
    pygame.time.wait(500)
    for i in self.directions:
      self.directions[i] = False
    self.directions['UP'] = True
