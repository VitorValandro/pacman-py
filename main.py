import pygame, sys
from pygame.locals import *

from screens.startGame import startGame
from screens.startMenu import menu

menu()
while True:
  gameResult = startGame()
  menu(message=gameResult[0], points=gameResult[1])
