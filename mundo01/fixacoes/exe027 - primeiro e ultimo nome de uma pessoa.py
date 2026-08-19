# strip vai remover os espaços extras das bordas
    # isso é, evitar que espaços soltos atrapalhem a separação
n = str(input('Digite seu nome completo: ')).strip()

# split vai separar o texto em partes, quebrando nos espaços
    # isso é, transformar o nome completo em uma lista com cada nome separado
nome = n.split()

print('Muito prazer em te conhecer!')

# nome[0] acessa o primeiro item da lista
    # isso é, pegar só o primeiro nome
print('Seu primeiro nome é {}'.format(nome[0]))

# len vai contar quantos itens tem na lista
# len(nome)-1 é o índice do último item, porque o Python começa a contar do 0
    # isso é, se a lista tem 3 nomes, o último está na posição 2
print('Seu último nome é {}'.format(nome[len(nome)-1]))
