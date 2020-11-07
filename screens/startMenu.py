import pygame, sys
from pygame.locals import *

from .startGame import printText

screenSize = WIDTH, HEIGTH = 800, 700

pygame.init()

window = pygame.display.set_mode(screenSize)

def menu(message='PACMAN', points=None):
  closeMenu = False
  pygame.display.flip()
  while not closeMenu:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == K_RETURN:
          closeMenu = True
    window.fill((0,0,0))
    if points != None:
      printText(window, message, (400, 100), 50, (255, 255, 255))
      printText(window, 'YOUR SCORE:', (400, 250), 40, (255, 255, 255))
      printText(window, str(points), (400, 300), 50, (255, 255, 255))
      printText(window, 'PRESS ENTER TO PLAY AGAIN', (400, 500), 40, (255, 255, 255))
      pygame.display.flip()
    else:
      printText(window, message, (400, 300), 50, (255, 255, 255))
      printText(window, 'PRESS ENTER TO START', (400, 350), 50, (255, 255, 255))
      pygame.display.flip()
