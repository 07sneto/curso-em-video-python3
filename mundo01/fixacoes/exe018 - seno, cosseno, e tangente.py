# math é o módulo de Matemática
    # radians vai converter graus para radianos.
    # sin vai calcular o seno do ângulo.
    # cos vai calcular o cosseno do ângulo.
    # tan vai calcular a tangente do ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
