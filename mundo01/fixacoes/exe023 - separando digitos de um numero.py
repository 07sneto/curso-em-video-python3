num = int(input('Digite um número: '))

# // é a divisão inteira e % é o resto da divisão
    # isso é, combinando os dois conseguimos isolar cada dígito do número

# // 1 divide por 1 (não muda nada) e % 10 pega o resto, que é o último dígito
u = num // 1 % 10

# // 10 joga fora a unidade, e % 10 pega o último dígito que sobrou
d = num // 10 % 10

# // 100 joga fora unidade e dezena, e % 10 pega o último dígito que sobrou
c = num // 100 % 10

# // 1000 joga fora tudo menos o milhar, e % 10 isola ele
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
