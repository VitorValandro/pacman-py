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
    if message == 'YOU WIN':
      printText(window, 'PACMAN', [400, 70], 50, (255, 199, 0), 'screens\pac-font.TTF')
      printText(window, message, (400, 170), 75, (255, 255, 255), 'screens\8-bit.TTF')
      printText(window, 'YOUR SCORE:', (400, 270), 40,(255, 255, 255), 'screens\8-bit.TTF')
      printText(window, str(points), (400, 320), 50,(255, 255, 255), 'screens\8-bit.TTF')
      printText(window, '1  2 3 4 5', [400, 420], 50, (255, 199, 0), 'screens\pac-font.TTF')
      printText(window, 'PRESS ENTER TO PLAY AGAIN', (400, 570), 40, (255, 255, 255), 'screens\8-bit.TTF')
      pygame.display.flip()
    if message == 'GAME OVER':
      printText(window, 'PACMAN', [400, 70], 50, (38, 2, 255), 'screens\pac-font.TTF')
      printText(window, message, (400, 170), 75, (255, 255, 255), 'screens\8-bit.TTF')
      printText(window, 'YOUR SCORE:', (400, 270), 40,(255, 255, 255), 'screens\8-bit.TTF')
      printText(window, str(points), (400, 320), 50,(255, 255, 255), 'screens\8-bit.TTF')
      printText(window, '9 9  1  9 9', [400, 420], 50, (38, 2, 255), 'screens\pac-font.TTF')
      printText(window, 'PRESS ENTER TO PLAY AGAIN', (400, 570), 40, (255, 255, 255), 'screens\8-bit.TTF')
      pygame.display.flip()
    else:
      printText(window, 'PACMAN', [400, 90], 60,(255, 199, 0), 'screens\pac-font.TTF')
      printText(window, '1', [200, 300], 90, (255, 199, 0), 'screens\pac-font.TTF')
      printText(window, '2 2 2 2', [410, 300], 90, (201, 0, 0), 'screens\pac-font.TTF')
      printText(window, '9', [600, 300],90, (38, 2, 255), 'screens\pac-font.TTF')
      printText(window, 'PRESS ENTER TO START GAME', (400, 540), 50, (255, 255, 255), 'screens\8-bit.TTF')
      pygame.display.flip()
