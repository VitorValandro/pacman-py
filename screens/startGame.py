'''
Este arquivo é responsável por rodar todo o jogo,
gerenciando o loop principal
'''
# Importa módulos externos #
import pygame, sys
from pygame.locals import *

# Importa arquivos locais #
from classes.maze import mazePix, pgMaze, generateCoins, ghostsMaze, generateCherry
from classes.pac import Pac, general_spritesheet
from classes.ghosts import Ghost, ghostNames
from .pauseGame import pauseGame, printText

screenSize = WIDTH, HEIGTH = 800, 700 # Dimensões da tela do pygame

pygame.init()

window = pygame.display.set_mode(screenSize)

def startGame(): # Função na qual se insere o loop principal
  state = 'RUNNING'
  closeGame = False
  FPS = 60
  clock = pygame.time.Clock() # Define o clock que controla a velocidade do loop

  PACMAN = Pac(mazePix) # Instancia o jogador
  ghosts = []
  ghostsRect = []
  for i in range(4): # Instancia os fantasmas
    ghosts.append(Ghost(ghostsMaze, ghostNames[i]))
    ghostsRect.append(ghosts[i].rect)

  coinsList = generateCoins() # Instancia as moedas
  rectCoinsList = []
  for i in coinsList:
    rectCoinsList.append(i.getRect())

  cherryList = []

  coinsCollected = 0
  Delay = 0
  spriteDelay = 0

  # Loop principal do jogo #
  while not closeGame: 
    time = clock.tick(FPS)

    # Controle de sprite split #
    PACMAN.sprite = PACMAN.spritesheet[PACMAN.frameCount]
    for ghost in ghosts:
      ghost.sprite = ghost.spritesheet[ghost.frameCount]

    Delay += time
    spriteDelay += time
    for event in pygame.event.get():  # Verifica os eventos do teclado do usuário
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        PACMAN.movement(event.key)
        if event.key == K_h:
          state = 'PAUSE'
          
    # Gerencia as entidades #
    if state == 'RUNNING':
      PACMAN.move()
      for ghost in ghosts:
        ghost.move()

      if Delay >= 1000: # A cada 1 segundo tenta mudar a direção do fantasma
        for ghost in ghosts:
          ghost.verifyChangePosition()

      if Delay >= 20000: # A cada 20 segundos gera uma cereja
        PACMAN.cherryPower(ghosts, False)
        if Delay >= 20000 and len(cherryList) < 2:
          cherryList.append(generateCherry())
          Delay = 1000
      
      rectCherryList = []
      for cherry in cherryList:
        rectCherryList.append(cherry.getRect())
        
      # Atualização de tela #
      window.fill((0, 0, 0))
      window.blit(pgMaze, (0, 0))

      for coin in coinsList:
        coin.renderCoin(window)

      window.blit(PACMAN.sprite, PACMAN.rect)
      for ghost in ghosts:
        window.blit(ghost.sprite, ghost.rect)
      for cherry in cherryList:
        window.blit(cherry.sprite, cherry.getRect())

      for i in range(PACMAN.lifes):
        window.blit(general_spritesheet.subsurface(
            Rect(25, 0, 25, 25)), Rect(175+i*35, 650, 25, 25))
      
      # Quadrados para suavizar o teletransporte do pacman
      pygame.draw.rect(window, (0, 0, 0), [647, 324, 55, 35])
      pygame.draw.rect(window, (0, 0, 0), [100, 324, 55, 35])

      # Textos da tela
      printText(window, str(coinsCollected), [
                600, 645], 40, (255, 255, 255), 'screens\8-bit.TTF')
      printText(window, 'PACMAN', [400, 30], 40,
                (255, 199, 0), 'screens\pac-font.TTF')

      # Verificação de colisão #
      coinCollideIndex = PACMAN.rect.collidelist(rectCoinsList)
      if coinCollideIndex != -1: # Verifica se todas as moedas foram coletadas
        del rectCoinsList[coinCollideIndex]
        del coinsList[coinCollideIndex]
        coinsCollected += 10
        if len(coinsList) == 0:
          return(("YOU WIN", coinsCollected))

      cherryCollideIndex = PACMAN.rect.collidelist(rectCherryList)
      if cherryCollideIndex != -1: # Verifica se o pacman comeu uma cereja
        del rectCherryList[cherryCollideIndex]
        del cherryList[cherryCollideIndex]
        PACMAN.cherryPower(ghosts, True) # Dá poder ao Pacman
        coinsCollected += 100
        Delay = 1000

      ghostCollideIndex = PACMAN.rect.collidelist(ghostsRect)
      if ghostCollideIndex != -1: # Verifica se o pacman se chocou com o fantasma
        if not PACMAN.invencibility:
          PACMAN.die()
          pygame.time.wait(500)
        else:
          ghosts[ghostCollideIndex].die()

      pygame.display.update()

      # Verifica se o jogador perdeu
      if PACMAN.lifes == 0:
        closeGame = True
        return(("GAME OVER", coinsCollected))

      # Atualiza o frame do sprite
      if spriteDelay >= 100:
        PACMAN.frameCount += 1
        ghost.frameCount += 1
        spriteDelay = 0
        
    # Pausa o jogo
    if state == 'PAUSE':
      state = pauseGame(state, window, coinsCollected)