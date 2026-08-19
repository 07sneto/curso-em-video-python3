# random é o módulo de aleatoriedade
    # shuffle vai embaralhar os elementos da lista.
        # isso é, colocar os itens em ordem aleatória.

from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
