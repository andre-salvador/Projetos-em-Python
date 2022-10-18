from cgitb import reset
from random import random
import os
import random
from colorama import Fore, Back, Style


def tela():
    global velha
    os.system('cls')
    print(f'jogadas: {Fore.GREEN + str(jogadas) + Fore.RESET}')
    print('    0   1   2')
    print(f'0   {velha[0][0]} | {velha[0][1]} | {velha[0][2]}')
    print(f'   {"-" * 11}')
    print(f'0   {velha[1][0]} | {velha[1][1]} | {velha[1][2]}')
    print(f'   {"-" * 11}')
    print(f'0   {velha[2][0]} | {velha[2][1]} | {velha[2][2]}')

jogar_novamente = 's'
jogadas = 0
quem_joga = 2
max_jogadas = 9
vit = 'n'
velha = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

while True:
    pass