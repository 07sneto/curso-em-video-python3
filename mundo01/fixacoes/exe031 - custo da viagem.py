dist = float(input('Qual é a distância da sua viagem? R$'))
print('Você está prestes a começar sua viagem de {}Km'.format(dist))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preço))
