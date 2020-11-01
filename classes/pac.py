import pygame, sys
from pygame.locals import *
from .maze import checkRoute
from .ghosts import spritesheets

pacman_spritesheet = pygame.image.load("spritesheet.png")

WHITE = (255, 255, 255, 255)
class Pac(pygame.sprite.Sprite):
  COLOR = (125, 125, 125)
  ACELERATION = 1
  directions = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def __init__(self, routeMap):
    super(Pac, self).__init__()
    self.spritesheet = getSpriteFrame('RIGHT')
    self.sprite = self.spritesheet[0]
    self.rect = self.sprite.get_rect()
    self.rect.center = (400, 500)
    self.routeMap = routeMap
    self.lifes = 3
    self.invencibility = False

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
      self.spritesheet = getSpriteFrame('UP')
    if self.directions['DOWN'] and checkRoute(self, 0, +1, self.routeMap, WHITE):
      self.rect.move_ip(0, self.ACELERATION)
      self.spritesheet = getSpriteFrame('DOWN')
    if self.directions['LEFT'] and checkRoute(self, -1, 0, self.routeMap, WHITE):
      self.rect.move_ip(-(self.ACELERATION), 0)
      self.spritesheet = getSpriteFrame('LEFT')
    if self.directions['RIGHT'] and checkRoute(self, +1, 0, self.routeMap, WHITE):
      self.rect.move_ip(self.ACELERATION, 0)
      self.spritesheet = getSpriteFrame('RIGHT')
    
    if self.routeMap[self.rect.center[0], self.rect.center[1]] == (255, 255, 255, 255):
      self.stopMove()
    
    if self.rect.right <= 155: #teletransporte do pacman
      self.rect.left = 650
    
    if self.rect.left >= 651:
      self.rect.right = 155
    
  def die(self):
    pygame.time.wait(500)
    self.stopMove()
    self.lifes -= 1
    self.rect.center = (400, 500)
  
  def cherryPower(self, ghostsList, flag):
    self.invencibility = flag
    if self.invencibility:
      for ghost in ghostsList:
        ghost.sprite = pygame.image.load("ghost_sprite2.jpg")
    else:
      for i in range(4):
        ghostsList[i].sprite = pygame.image.load(spritesheets[i])
      
def getSpriteFrame(direction):
  if direction == 'RIGHT':
    startY = 0
  if direction == 'LEFT':
    startY = 25
  if direction == 'UP':
    startY = 50
  if direction == 'DOWN':
    startY = 75
  
  pacman_frames = [
      pacman_spritesheet.subsurface(Rect(0, startY, 25, 25)),
      pacman_spritesheet.subsurface(Rect(25, startY, 25, 25)),
      pacman_spritesheet.subsurface(Rect(50, startY, 25, 25)),
      pacman_spritesheet.subsurface(Rect(75, startY, 25, 25)),
  ]

  return pacman_frames
