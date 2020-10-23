import pygame, sys
from pygame.locals import *
from PIL import Image

maze = Image.open('mazeRoute.png')
mazePix = maze.load()
print('Image size: ', maze.size)
pgMaze = pygame.image.load('mazeGraph.png')