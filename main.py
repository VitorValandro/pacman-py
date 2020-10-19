'''
TO DO:
- Terminar de desenhar o tabuleiro no figma e passar pra lista
'''

import pygame, sys
from pygame.locals import *
from classes.table import TableRect, POSITIONS
from classes.pac import Pac

screenSize = WIDTH, HEIGTH = 800, 600

pygame.init()

window = pygame.display.set_mode(screenSize)

tableRectsList = []
tableCollideList = []

FPS = 60
clock = pygame.time.Clock()

for pos in POSITIONS:
  positions = []
  for i in range(0,4):
    positions.append(pos[i])
  tableRectsList.append(TableRect(positions[0], positions[1], positions[2], positions[3]))

for i in tableRectsList:
  tableCollideList.append(i.get_rect())

PACMAN = Pac(400, 400, 25, 25)

while True:
  clock.tick(FPS)

  for event in pygame.event.get(): #verifica os eventos do teclado do usuário
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      PACMAN.movement(event.key)
  
  PACMAN.move()
  
  if PACMAN.get_rect().collidelist(tableCollideList) != -1:
    PACMAN.stopMove()

  window.fill((0,0,0))
  for i in tableRectsList:
    i.drawTable(window)
  
  PACMAN.drawPac(window)
  pygame.display.update()
