import sys

from fizzBuzzKata import fizzBuzz
from fizzBuzzKata.fizzBuzz import Game

newGame = Game(1)

print(f'Bienvenue dans le jeu')
print(f'')
print(f'Papier: p - Caillou: r - Ciseaux: s ?')
print(f'')
print(f'q pour quitter le jeu')
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
#     print(f'Score: ' + newGame.startgame())

print("Exit")