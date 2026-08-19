nome = str(input('Qual é seu nome? '))

# Isto é uma Condição Aninhada
if nome == 'Neto':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
