# upper vai transformar o texto em maiúsculas
    # isso é, garantir que tudo fique em CAIXA ALTA antes de analisar
# strip vai remover os espaços extras das bordas
    # isso é, evitar que espaços soltos atrapalhem a contagem
frase = input('Digite uma frase: ').upper().strip()

# count vai contar quantas vezes um caractere aparece no texto
    # isso é, ele percorre a frase inteira procurando a letra A e soma todas as ocorrências
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

# find vai procurar a primeira ocorrência de um caractere e retornar sua posição
    # isso é, ele começa do início e para no primeiro A que encontrar
# +1 é porque o Python começa a contar do 0, mas para nós o primeiro caractere é a posição 1
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

# rfind faz o mesmo que find, mas começa a busca pelo final do texto
    # isso é, ele acha o último A da frase em vez do primeiro
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
