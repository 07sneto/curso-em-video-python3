cid = str(input('Em que cidade você nasceu? '))

# cid[:5] é um fatiamento de string, pegando do índice 0 até o 4
    # isso é, pegar só os 5 primeiros caracteres do que foi digitado
# upper transforma em maiúsculas para a comparação não depender de como o usuário digitou
    # isso é, 'santo', 'Santo' e 'SANTO' viram todos 'SANTO' antes de comparar
# == verifica se os dois lados são iguais, retornando True ou False
    # isso é, o print vai mostrar True se a cidade começar com Santo, e False se não começar
print(cid[:5].upper() == 'SANTO')
