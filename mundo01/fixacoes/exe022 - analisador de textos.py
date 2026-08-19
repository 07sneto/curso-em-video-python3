# strip vai remover os espaços extras das bordas do texto
        # isso é, tirar espaços que ficam no começo ou no fim do que foi digitado
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

# upper vai transformar o texto em letras maiúsculas
    # isso é, colocar tudo em CAIXA ALTA
print('Seu nome em maiúsculas: {}'.format(nome.upper()))

# lower vai transformar o texto em letras minúsculas
    # isso é, colocar tudo em caixa baixa
print('Seu nome em minúsculas: {}'.format(nome.lower()))

# len vai contar quantos caracteres tem no texto
# count vai contar quantas vezes um caractere aparece
    # isso é, len conta tudo, e count conta só os espaços, aí subtraímos para contar só as letras
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# split vai separar o texto em partes, quebrando nos espaços
    # isso é, transformar o nome completo em uma lista com cada nome separado
separa = nome.split()

# separa[0] acessa o primeiro item da lista
    # isso é, pegar só o primeiro nome
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
