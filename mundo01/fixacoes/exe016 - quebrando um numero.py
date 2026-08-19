# math é o módulo de Matemática
    # trunc vai truncar um número.
        # isso é, mostrar somente a parte inteira do valor.

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
