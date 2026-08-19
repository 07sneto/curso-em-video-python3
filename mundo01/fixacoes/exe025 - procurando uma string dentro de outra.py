nome = str(input('Qual é seu nome completo? ')).strip()

# in verifica se um texto está dentro de outro, retornando True ou False
    # isso é, ele vai procurar 'silva' dentro do nome e dizer se achou ou não
# lower é usado antes de comparar para ignorar maiúsculas e minúsculas
    # isso é, 'Silva', 'SILVA' e 'silva' viram todos 'silva' antes de procurar
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
