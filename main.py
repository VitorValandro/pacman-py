import pygame, sys
from pygame.locals import *
from classes.table import mazePix, pgMaze
from classes.pac import Pac

screenSize = WIDTH, HEIGTH = 800, 700

pygame.init()

window = pygame.display.set_mode(screenSize)

FPS = 60
clock = pygame.time.Clock()

PACMAN = Pac(mazePix)

while True:
  clock.tick(FPS)

  for event in pygame.event.get(): #verifica os eventos do teclado do usuário
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      PACMAN.movement(event.key)

  PACMAN.move()

  window.fill((0,0,0))
  #window.blit(pgMaze, (155, 70))
  window.blit(pgMaze, (0, 0))
  window.blit(PACMAN.sprite, PACMAN.rect)
  pygame.display.update()
