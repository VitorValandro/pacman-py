'''
Este arquivo é responsável por gerenciar
todas as funcionalidades envolvendo os fantasmas
'''

# Importando módulos externos #
import pygame, sys
from pygame.locals import *
import random

# Importando arquivos locais #
from .maze import checkRoute

# Carrega a spritesheet para splitar
general_spritesheet = pygame.image.load("spritesheet.png")

WHITE = (255, 255, 255, 255)
ghostNames = ['Blinky', 'Clyde', 'Pinky', 'Inky']

# Classe principal dos fantasmas
class Ghost(pygame.sprite.Sprite):
  VELOCITY = 1 
  def __init__(self, routeMap, name): # Método construtor
    super().__init__()
    self.name = name
    self.scared = False
    # Inicia com o sprite do fantasma olhando pra cima
    self.spritesheet = ghostGetSpriteFrame('UP', self.name, self.scared) 
    self.sprite = self.spritesheet[0]
    self.rect = self.sprite.get_rect()
    self.rect.center = (399, 338) # Posição inicial do fantasma
    self.routeMap = routeMap # Carrega a rota que os fantasmas podem seguir
    self.changePosition = True
    self.frameCount = 0
    self.directions = {'UP': True, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

  def verifyChangePosition(self): # Altera a flag para mudar a posição
    if self.changePosition == True:
      self.changePosition = False
    else:
      self.changePosition = True

  def direcoesPossiveis(self, oldDirection='', directionArray=''): # Verifica quais as posições possíveis de seguir
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

  def changeDirection(self): # Verifica todas as direções que o fantasma pode seguir e decide randomicamente
    oldDirection = '' 
    for i in self.directions:
      if self.directions[i]:
        oldDirection = i # Armazena a direção que o fantasma estava seguindo
    possibleDirections = self.direcoesPossiveis(oldDirection=oldDirection, directionArray=self.directions)

    if len(possibleDirections):
      randomDirection = random.choice(possibleDirections)
      if randomDirection == oldDirection and len(possibleDirections) >= 3:
        randomDirection = random.choice(possibleDirections)
      self.directions[randomDirection] = True

  def move(self): # Troca a posição do fantasma a cada ciclo
    if self.frameCount >= 1: # Troca o frame do sprite
      self.frameCount = 0

    for i in self.directions:
      if self.directions[i]:
        oldDirection = i
    if self.directions['UP'] and checkRoute(self, 0, -1, self.routeMap, WHITE):
      self.rect.move_ip(0, -(self.VELOCITY))
      self.spritesheet = ghostGetSpriteFrame('UP', self.name, self.scared)
    if self.directions['DOWN'] and checkRoute(self, 0, +1, self.routeMap, WHITE):
      self.rect.move_ip(0, self.VELOCITY)
      self.spritesheet = ghostGetSpriteFrame('DOWN', self.name, self.scared)
    if self.directions['LEFT'] and checkRoute(self, -1, 0, self.routeMap, WHITE):
      self.rect.move_ip(-(self.VELOCITY), 0)
      self.spritesheet = ghostGetSpriteFrame('LEFT', self.name, self.scared)
    if self.directions['RIGHT'] and checkRoute(self, +1, 0, self.routeMap, WHITE):
      self.rect.move_ip(self.VELOCITY, 0)
      self.spritesheet = ghostGetSpriteFrame('RIGHT', self.name, self.scared)
    
    if len(self.direcoesPossiveis()) >= 2 and not oldDirection in self.direcoesPossiveis():
      if self.changePosition == True:
        self.changeDirection()
        self.changePosition = False
      
    elif len(self.direcoesPossiveis()) >= 3:
        self.changeDirection()

    if self.rect.right <= 155:  # Teletransporte do fantasma quando atinge a borda
      self.rect.left = 650

    if self.rect.left >= 651:
      self.rect.right = 155
    
    if self.rect.center == (399, 341): # Verifica se ele está no ponto de início
      for i in self.directions:
        self.directions[i] = False
      self.directions['UP'] = True

  def die(self): # Método que retorna ele para sua posição inicial
    self.rect.center = (399, 338)
    pygame.time.wait(500)
    for i in self.directions:
      self.directions[i] = False
    self.directions['UP'] = True
  
def ghostGetSpriteFrame(direction, name, scared): # Método para gerenciar o split da spritesheet
  yPos = {'RIGHT': 0, 'LEFT': 25, 'UP': 50, 'DOWN': 75}
  xPos = {'Blinky': 100, 'Clyde': 150, 'Pinky': 200, 'Inky': 250}
  if scared:
    ghost_frames = [
      general_spritesheet.subsurface(Rect(0, 100, 25, 25)),
      general_spritesheet.subsurface(Rect(24, 100, 25, 25)),
    ]
  else:
    startY = yPos[direction]
    startX = xPos[name]

    ghost_frames = [
        general_spritesheet.subsurface(Rect(startX, startY, 25, 25)),
        general_spritesheet.subsurface(Rect(startX+24, startY, 25, 25)),
    ]

  return ghost_frames
