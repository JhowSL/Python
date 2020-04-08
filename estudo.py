"""
n1 = int(input())
n2 = int(input())
s = n1 + n2
print('A soma de {} e de {} é equivalente à {}.'.format(n1, n2, s))
"""
"""
.isnumeric = se é numero
.isalpha = se é letra
.isalanum =  se é letra e numero 
.isupper =  se está somente em letra maiuscula
.islower =  se está em letra minuscula
.istitle =  se está capitalizada (maiuscula e minuscula)
.isspace = se tem espaços  
"""
"""
# Desafio 04 - Guanabara

a = input('Digite algo: ')
print('A classe desse valor é {}'.format(type(a)))
print('A classe só tem espaços? {}'.format(a.isspace()))
print('A classe é um número? {}'.format(a.isnumeric()))
print('A classe é alfebetica? {}'.format(a.isalpha()))
print('A classe é alfanumérica? {}'.format(a.isalnum()))
print('A classe está em maiúscula? {}'.format(a.isupper()))
print('A classe está em minúscula? {}'.format(a.islower()))
print('A classe está capitalizada? {}'.format(a.istitle()))
"""
"""
Ordem de precedência
1: ()
2: **
3: *, /, //, %
4: +, -
"""
"""
'='*20
repete o que está dentro do paranteses * a quantidade pedida
{:20} = numero de espaços
{:>20} = alinhamento para direita em 20 espaços
{:<20} = alinhamento para esquerda em 20 espaços
{:^20} = alinhamento central em 20 espaços
{:=^20}: = alinhamento central em 20 espaços com iguais(ou em alguma coisa do ^) antes do em volta

nome = input('Qual o meu nome? ')
print('Então eu sou o famoso {:_^10}!'.format(nome))
"""
"""
n1 = int(input('Primeiro valor: '))
n2 = int(input('segundo valor: '))

so = n1 + n2
su = n1 - n2
mu = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
e = n1 ** n2

print('A soma de {} + {} é {}, \n a subtração é {}, \n a multiplicação é {} e a expoentização é {}.'
      .format(n1, n2, so, su, mu, e), end=' ')
print('\n A divisão é {}, \n e sua divisão inteira é de {}, \n e o resto será de {}.'.format(d, di, re))
"""

# Desafio 005 - Antecessor e sucessor

n = int(input('Digite um número: '))
print('O antecessor de {} é {} e o seu posterior é {}.'.format(n, n-1, n+1))
# print('\n O antecessor de {} é:\n {}\n e o seu posterior é:\n {}.'.format(n, n-1, n+1))
