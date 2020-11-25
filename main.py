'''
Arquivo principal

RODE ESTE ARQUIVO PARA INICIAR O JOGO
'''

# Importa os arquivos locais usados #
from screens.startGame import startGame
from screens.startMenu import menu

menu()
while True:
  gameResult = startGame()
  menu(message=gameResult[0], points=gameResult[1])
