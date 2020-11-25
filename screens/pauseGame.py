'''
Arquivo que gerencia a tela de pause do jogo
'''

import pygame, sys
from pygame.locals import *

def pauseGame(state, window, coinsCollected):
  while state == 'PAUSE':
    pygame.display.flip()
    window.fill((0, 0, 0))
    printText(window, 'PACMAN', [400, 70], 50,
              (255, 199, 0), 'screens\pac-font.TTF')
    printText(window, 'GAME PAUSED', (400, 170), 75,
              (255, 255, 255), 'screens\8-bit.TTF')
    printText(window, str(coinsCollected), (400, 260),
              40, (38, 2, 255), 'screens\8-bit.TTF')
    printText(window, 'Avoid the ghosts and', (400, 320),
              40, (255, 255, 255), 'screens\8-bit.TTF')
    printText(window, 'eat all coins to win', (400, 360),
              40, (255, 255, 255), 'screens\8-bit.TTF')
    printText(window, 'Movement -> Arrow Keys', (400, 420),
              40, (255, 255, 255), 'screens\8-bit.TTF')
    printText(window, 'Power -> Eat Cherry', (400, 460),
              40, (255, 255, 255), 'screens\8-bit.TTF')
    printText(window, 'PRESS H TO BACK GAME', (400, 570),
              50, (255, 255, 255), 'screens\8-bit.TTF')
    pygame.display.flip()
    for event in pygame.event.get():  # verifica os eventos do teclado do usuário
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == K_h:
          state = 'RUNNING'
  return state

def printText(display, text, midtop, size, color, font):  # Função para printar texto na tela
  font = pygame.font.Font(font, size)
  printFont = font.render(text, 1, color)
  fontArea = printFont.get_rect()
  fontArea.midtop = midtop
  display.blit(printFont, fontArea)
