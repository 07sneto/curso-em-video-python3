from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogadaUser = int(input('Qual é a sua jogada? ')) - 1
jogadaCpu = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 16)
print('Jogador jogou {}'.format(itens[jogadaUser]))
print('Computador jogou {}'.format(itens[jogadaCpu]))
print('-=' * 16)

if jogadaCpu == 0:
    if jogadaUser == 0:
        print('EMPATE')
    elif jogadaUser == 1:
        print('JOGADOR VENCE')
    elif jogadaUser == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')
elif jogadaCpu == 1:
    if jogadaUser == 0:
        print('COMPUTADOR VENCE')
    elif jogadaUser == 1:
        print('EMPATE')
    elif jogadaUser == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida.')
elif jogadaCpu == 2:
    if jogadaUser == 0:
        print('JOGADOR VENCE')
    elif jogadaUser == 1:
        print('COMPUTADOR VENCE')
    elif jogadaUser == 2:
        print("EMPATE")
    else:
        print('Jogada inválida.')
