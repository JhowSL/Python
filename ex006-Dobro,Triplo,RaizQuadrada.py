# Desafio 006 - Dobro, Triplo, Raiz Quadrada
# importar pasta math
from math import *

# Entrada
n = int(input('Insira um número: '))
# Solução
d = n * 2
t = n * 3
q = sqrt(n)
# Saida
print('Já que o dobro de {:.0f} é de {:.0f}, o triplo será {:.0f} e a sua raiz quadrada será de {:.2f}.'.format(n, d, t,
                                                                                                                q))
# Sair do programa
input()
