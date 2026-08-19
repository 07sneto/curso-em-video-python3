# random é o módulo de aleatoriedade
from random import randint

# time, sleep, faz com que o programe dê uma certa pausa por segundos determinados pelo codigo
from time import sleep

# vai fazer com que sorteie um número entre 0 e 5 aleatorio, e guarde na variavel computador
computador = randint(0, 5)

print('-' * 40)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 40)

jogador = int(input('Em que número eu pensei? ')) #aqui, o user tenta adivinhar o número sorteado
print('PROCESSANDO...')
sleep(3) # aqui o programa da uma pausa por 3 segundos

if jogador == computador:
    print('Acertou! Você ganhou de mim!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
