#Ex4 - Aqui é utilizado o método capitalize para fazer com que a primeira letra da variavel frase3 torne-se maiuscula e depois é feito uma lista l3 da variavel frase4. Ainda, é utilizado um método append ('') como recurso para resolução do exercício.
frase3 = input('Digite uma frase que gostaria de que a primeira letra de cada palavra fique em maiúscula: ')
frase4 = frase3.capitalize()
l3 = list(frase4.split())
l3.append('')
#Criação do laço for e de uma estrutura if em que será testado as condições em que a próxima letra após a pontuação deva ser maiuscula. Em caso positivo, vai ser inserido a palavra com ela maiuscula e em sequência a deleção da palavra minuscula, mantendo o sentido da frase.
for m in range(len(l3)):
    if (l3[m].endswith('.')) or (l3[m].endswith('!')) or (l3[m].endswith('?')):
        l3.insert(m + 1, l3[m + 1].capitalize())
        del l3[m+2]
print(' '.join(l3))

