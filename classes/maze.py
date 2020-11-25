'''
Este arquivo é responsável por gerenciar
tudo que envolve os labirintos (gráficos e lógicos)
e suas entidades
'''

# Importa módulos externos #
import pygame, sys
from pygame.locals import *
from PIL import Image
import random

general_spritesheet = pygame.image.load("spritesheet.png")

maze = Image.open('mazeRoute.png') # Imagem da rota a ser seguida pelo pacman
mazePix = maze.load()
print('Image size: ', maze.size)
pgMaze = pygame.image.load('mazeGraph.png') # Imagem gráfica do labirinto
ghostsMa = Image.open('mazeRouteGhosts.png') # Imagem da rota a ser seguida pelos fantasmas
ghostsMaze = ghostsMa.load()

class Coin: # Classe das moedas que são comidas pelo pacman
  COLOR = (255, 199, 0)
  WIDTH, HEIGTH = 4, 4

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def renderCoin(self, surface): # Pinta as moedas no labirinto
    pygame.draw.rect(surface, self.COLOR, [self.x, self.y, self.WIDTH, self.HEIGTH])
  
  def getRect(self): # Fornece o quadrado para analisar colisão
    return pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGTH)

class Cherry: # Classe para as cerejas que dão superpoder pro pacman
  COLOR = (255, 0, 0)
  WIDTH, HEIGTH = 10, 10

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.sprite = general_spritesheet.subsurface(Rect(50, 100, 25, 25))

  def getRect(self):  # Fornece o quadrado para analisar colisão
    return pygame.Rect(self.x-12, self.y-12, 25, 25)


def generateCoins(): # Inicia as posições das moedas quando o jogo começa
  x = 0
  coinsList = []
  while x <= 50:
    y = 0
    while y <= 50:
      if mazePix[159+x*10, 112+y*10] == (0,0,0,255):
        coinsList.append(Coin(159+x*10, 112+y*10))
      y+=1
    x+=1
  return coinsList

def generateCherry(): # Função chamada toda vez que uma cereja deve ser gerada
  cherryList = []
  x = random.randint(0, 50)
  y = random.randint(0, 50)
  while mazePix[159+x*10, 112+y*10] != (0, 0, 0, 255):
    x = random.randint(0, 50)
    y = random.randint(0, 50)

  return Cherry(159+x*10, 112+y*10)

def checkRoute(obj, xAdd, yAdd, routeMap, color, equal=False): # Checa a cor da imagem da rota das entidades
  if equal: # Analisa se a operação é igual (==) ou diferente (!=)
    if routeMap[obj.rect.center[0]+xAdd, obj.rect.center[1]+yAdd] == color:
      return True
    return False
  else:
    if routeMap[obj.rect.center[0]+xAdd, obj.rect.center[1]+yAdd] != color:
      return True
    return False
