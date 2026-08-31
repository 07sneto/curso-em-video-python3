from random import randint

print('Sou seu computador...')
numeroCpu = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi? ')

acertou = False
tentativasUser = 0

while not acertou:
    palpiteUser = int(input('Qual é seu palpite? '))
    tentativasUser += 1
    if palpiteUser == numeroCpu:
        acertou = True
    else:
        if palpiteUser < numeroCpu:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('=' * 30)
print('Acertou com {} tentativas. Parabéns!'.format(tentativasUser))
