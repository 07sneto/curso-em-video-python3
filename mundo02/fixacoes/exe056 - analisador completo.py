somaIdade = 0
mediaIdade = 0

maiorIdadeHomem = 0
homemVelho = ''

totalMulher20 = 0

for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade

    if p == 1 and sexo == 'Mm':
        maiorIdadeHomem = idade
        homemVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        homemVelho = nome

    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1

mediaIdade += somaIdade / 4
print('----- RESULTADO -----')
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, homemVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher20))
