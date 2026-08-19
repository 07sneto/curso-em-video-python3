from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Ano de Nascimento: '))

idade = anoAtual - anoNasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Caregoria: MIRIM')
elif idade <= 14:
    print('Caregoria: INFANTIL')
elif idade <= 19:
    print('Caregoria: JUNIOR')
elif idade <= 25:
    print('Caregoria: SÊNIOR')
else:
    print('Caregoria: MASTER')
