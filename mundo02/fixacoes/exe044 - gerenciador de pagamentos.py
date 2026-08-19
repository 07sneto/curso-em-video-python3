print('{:-^40}'.format(' LOJAS SN '))
preco = float(input('Preço das compras: R$'))

print('''FORMA DE PAGAMENTO
[ 1 ] - á vista dinheiro/cheque
[ 2 ] - á vista cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcela = int(input('Quantas parcelas? '))
    parcela = total / totalParcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalParcela, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
