'''
TO DO:
- Fazer o clock do jogo
- Terminar de desenhar o tabuleiro no figma e passar pra lista
'''

import pygame, sys
from pygame.locals import *
from classes.table import TableRect, POSITIONS

screenSize = WIDTH, HEIGTH = 800, 500

pygame.init()

window = pygame.display.set_mode(screenSize)

tableRectsList = []
tableCollideList = []

for pos in POSITIONS:
  positions = []
  for i in range(0,4):
    positions.append(pos[i])
  tableRectsList.append(TableRect(positions[0], positions[1], positions[2], positions[3]))

while True:
  for i in tableRectsList:
    i.drawTable(window)
    tableCollideList.append(i.get_rect())

  

  pygame.display.flip()

  for event in pygame.event.get(): #verifica os eventos do teclado do usuário
    if event.type == QUIT:
      pygame.quit()
      sys.exit()