n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaointeira = n1 // n2
exponencial = n1 ** n2
print('A soma é {}, a Multiplicação é {}, a Divisão é {}'.format(soma, multiplicacao, divisao), end=' >>> ')
print('Divisão inteira é {} e Potência {}'.format(divisaointeira, exponencial))