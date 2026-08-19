salarioAtual = float(input('Qual é o salário do funcionário? R$'))

if salarioAtual <= 1250:
    salarioNovo = salarioAtual + (salarioAtual * 15 / 100)
else:
    salarioNovo = salarioAtual + (salarioAtual * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(salarioAtual, salarioNovo))
