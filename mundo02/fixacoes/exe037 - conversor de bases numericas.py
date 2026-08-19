inteiro = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
opcao = int(input('Sua opçao:'))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(inteiro, bin(inteiro)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(inteiro, oct(inteiro)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal a {}'.format(inteiro, hex(inteiro)[2:]))
else:
    print('Opção invalida! Tente novamente.')
