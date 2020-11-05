import pygame, sys
from pygame.locals import *

from screens.startGame import startGame
from screens.startMenu import menu

menu()
while True:
  menu(message=startGame())