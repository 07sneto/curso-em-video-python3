# random é o módulo de aleatoriedade
    # choice vai escolher um elemento aleatório.
        # isso é, pegar um item qualquer da lista.

from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
