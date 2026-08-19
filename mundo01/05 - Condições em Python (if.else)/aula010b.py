n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi de {:.1f}'.format(media))

if media >= 6:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, Estude mais!')
