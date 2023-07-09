#Resolução do Exercício 1, utilizando-se os métodos split para separar cada palavra digita em um valor de uma lista. Depois, o método reverse par que seja invertida a frase, independente do que seja escrito.
frase = input('Digite aqui a frase que deseja que seja invertida: ')
l = []
l = frase.split()
l.reverse()
#Utilização do laço for para que seja impresso uma palavra por vez e da função end para que tudo seja impresso na mesma linha.
for i in range(len(l)):
    print(l[i], end=' ')
print()

