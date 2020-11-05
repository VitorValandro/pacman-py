import pygame, sys
from pygame.locals import *

from .startGame import printText

screenSize = WIDTH, HEIGTH = 800, 700

pygame.init()

window = pygame.display.set_mode(screenSize)

def menu(message='PACMAN'):
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
    printText(window, message, (240, 320), 30, (255, 255, 255))
    printText(window, 'PRESS ENTER TO START', (240, 350), 30, (255, 255, 255))
    pygame.display.flip()
