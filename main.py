import pygame, sys
from pygame.locals import *
from classes.maze import mazePix, pgMaze, coinsList, rectCoinsList, ghostsMaze
from classes.pac import Pac
from classes.ghosts import Ghost

screenSize = WIDTH, HEIGTH = 800, 700

pygame.init()

window = pygame.display.set_mode(screenSize)

FPS = 60
clock = pygame.time.Clock()

PACMAN = Pac(mazePix)
Ghost1 = Ghost(ghostsMaze)
Ghost2 = Ghost(ghostsMaze)
Ghost3 = Ghost(ghostsMaze)
Ghost4 = Ghost(ghostsMaze)

def printText(display, text, midtop, size, color):  # function to write a text on screen
    font = pygame.font.get_default_font()
    standardFont = pygame.font.SysFont(font, size)
    printFont = standardFont.render(text, 1, color)
    fontArea = printFont.get_rect()
    fontArea.midtop = midtop
    display.blit(printFont, fontArea)

coinsCollected = 0
ghostDelay = 0
while True:
  time = clock.tick(FPS)

  ghostDelay += time
  for event in pygame.event.get(): #verifica os eventos do teclado do usuário
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      PACMAN.movement(event.key)

  PACMAN.move()
  Ghost1.move()
  Ghost2.move()
  Ghost3.move()
  Ghost4.move()

  if ghostDelay >= 1000:
    Ghost1.verifyChangePosition()

  window.fill((0,0,0))
  #window.blit(pgMaze, (155, 70))
  window.blit(pgMaze, (0, 0))

  for i in coinsList:
    i.renderCoin(window)

  coinCollideIndex = PACMAN.rect.collidelist(rectCoinsList)
  if coinCollideIndex != -1:
    del rectCoinsList[coinCollideIndex]
    del coinsList[coinCollideIndex]
    coinsCollected += 10

  window.blit(PACMAN.sprite, PACMAN.rect)
  window.blit(Ghost1.sprite, Ghost1.rect)
  window.blit(Ghost2.sprite, Ghost2.rect)
  window.blit(Ghost4.sprite, Ghost3.rect)
  window.blit(Ghost4.sprite, Ghost4.rect)

  pygame.draw.rect(window, (0,0,0), [647, 324, 55, 35]) # quadrados para suavizar o teletransporte do pacman
  pygame.draw.rect(window, (0,0,0), [100, 324, 55, 35])
  printText(window, str(coinsCollected), [750, 650], 30, (255, 255, 255))
  pygame.display.update()
