# math é o módulo de Matemática
    # hypot vai calcular a hipotenusa.
        # isso é, descobrir o tamanho do lado maior do triângulo.


from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
