import pygame, sys
from pygame.locals import *
from PIL import Image

maze = Image.open('mazeRoute.png') #imagem da rota a ser seguida pelas entidades
mazePix = maze.load()
print('Image size: ', maze.size)
pgMaze = pygame.image.load('mazeGraph.png') #imagem gráfica do labirinto

class Coin:
  COLOR = (255, 199, 0)
  WIDTH, HEIGTH = 4, 4

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def renderCoin(self, surface): #pintar as moedas no labirinto
    pygame.draw.rect(surface, self.COLOR, [self.x, self.y, self.WIDTH, self.HEIGTH])
  
  def getRect(self): #fornecer o quadrado para analisar colisão
    return pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGTH)

def generateCoins(): #inicia as posições das moedas quando o jogo começa
  x = 0
  coinsList = []
  while x <= 50:
    y = 0
    while y <= 50:
      if mazePix[179+x*10, 112+y*10] == (0,0,0,255):
        coinsList.append(Coin(179+x*10, 112+y*10))
      y+=1
    x+=1
  return coinsList

coinsList = generateCoins()
rectCoinsList = []
for i in coinsList:
  rectCoinsList.append(i.getRect())

def checkRoute(obj, xAdd, yAdd, routeMap, color, equal=False): #checa a cor da imagem da rota das entidades
  if equal: #analisa se a operação é igual (==) ou diferente (!=)
    if routeMap[obj.rect.center[0]+xAdd, obj.rect.center[1]+yAdd] == color:
      return True
    return False
  else:
    if routeMap[obj.rect.center[0]+xAdd, obj.rect.center[1]+yAdd] != color:
      return True
    return False
