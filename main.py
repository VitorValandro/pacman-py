import pygame, sys
from pygame.locals import *
from classes.maze import mazePix, pgMaze, coinsList, rectCoinsList, ghostsMaze, generateCherry, cherryList
from classes.pac import Pac
from classes.ghosts import Ghost, ghostNames

screenSize = WIDTH, HEIGTH = 800, 700

pygame.init()

window = pygame.display.set_mode(screenSize)

FPS = 60
clock = pygame.time.Clock()

PACMAN = Pac(mazePix)
ghosts = []
ghostsRect = []
for i in range(4):
  ghosts.append(Ghost(ghostsMaze, ghostNames[i])) 
  ghostsRect.append(ghosts[i].rect)

def printText(display, text, midtop, size, color):  # function to write a text on screen
    font = pygame.font.get_default_font()
    standardFont = pygame.font.SysFont(font, size)
    printFont = standardFont.render(text, 1, color)
    fontArea = printFont.get_rect()
    fontArea.midtop = midtop
    display.blit(printFont, fontArea)

coinsCollected = 0
Delay = 0
spriteDelay = 0

while True:
  time = clock.tick(FPS)
  PACMAN.sprite = PACMAN.spritesheet[PACMAN.frameCount]
  for ghost in ghosts:
    ghost.sprite = ghost.spritesheet[ghost.frameCount]

  Delay += time
  spriteDelay += time
  for event in pygame.event.get(): #verifica os eventos do teclado do usuário
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      PACMAN.movement(event.key)

  PACMAN.move()
  for ghost in ghosts:
    ghost.move()

  if Delay >= 1000:
    for ghost in ghosts:
      ghost.verifyChangePosition()
  
  if Delay >= 10000:
    PACMAN.cherryPower(ghosts, False)
    if Delay >= 20000 and len(cherryList) < 2:
      cherryList.append(generateCherry())
      Delay = 1000

  window.fill((0,0,0))
  #window.blit(pgMaze, (155, 70))
  window.blit(pgMaze, (0, 0))

  for coin in coinsList:
    coin.renderCoin(window)

  coinCollideIndex = PACMAN.rect.collidelist(rectCoinsList)
  if coinCollideIndex != -1:
    del rectCoinsList[coinCollideIndex]
    del coinsList[coinCollideIndex]
    coinsCollected += 10
  
  rectCherryList = []
  for cherry in cherryList:
    rectCherryList.append(cherry.getRect())
  cherryCollideIndex = PACMAN.rect.collidelist(rectCherryList)
  if cherryCollideIndex != -1:
    del rectCherryList[cherryCollideIndex]
    del cherryList[cherryCollideIndex]
    PACMAN.cherryPower(ghosts, True)
    Delay = 1000
  
  ghostCollideIndex = PACMAN.rect.collidelist(ghostsRect)
  if ghostCollideIndex != -1:
    if not PACMAN.invencibility:
      PACMAN.die()
      pygame.time.wait(500)
    else:
      ghosts[ghostCollideIndex].die()

  window.blit(PACMAN.sprite, PACMAN.rect)
  for ghost in ghosts:
    window.blit(ghost.sprite, ghost.rect)
  for cherry in cherryList:
    window.blit(cherry.sprite, cherry.getRect())

  pygame.draw.rect(window, (0,0,0), [647, 324, 55, 35]) # quadrados para suavizar o teletransporte do pacman
  pygame.draw.rect(window, (0,0,0), [100, 324, 55, 35])
  printText(window, str(coinsCollected), [750, 650], 30, (255, 255, 255))
  pygame.display.update()

  if spriteDelay >= 100:
    PACMAN.frameCount += 1
    ghost.frameCount += 1
    spriteDelay = 0