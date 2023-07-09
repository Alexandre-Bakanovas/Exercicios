#Ex5 Utilizando-se do código escrito no exercicio 3, com algumas pequenas modificações, foi possível criar o código abaixo. Nele, é pedido para que se digite uma palavra a qual quer ser testado a condição de palindro igual, ou seja, a palavra toda é o palindromo, e não somente suas partes. Para isso, foi definido uma variavel global, a var_global, a qual recebe a string inserida no começo do programa.

def palindromo():
    tamanho = input('Digite uma palavra para verificar se ela possui palindromo: ')
    global var_global
    var_global = tamanho
    length = len(tamanho)
    palindromos = []
    for x in range(2,length+1):
        min = 0
        high = x
        while high < length+1:
            testString = tamanho[min:high]
            if(len(testString)%2==0):
                midPoint = len(testString)//2
                if( testString[0:midPoint] == testString[midPoint:][::-1] ):
                    palindromos.append(testString)
            else:
                midPoint = len(testString)//2
                if(testString[0:midPoint] == testString[(midPoint+1):][::-1]):
                    palindromos.append(testString)
            min = min+1
            high = high + 1
    return palindromos

#Inicio do programa.
nome = palindromo()
#Neste caso, se a variavel global var_global, ou seja, a string digitada no começo, estiver dentro da lista gerada pela função palindromo, ela retornará a mensagem 'verdadeiro'. Caso negativo, resultará que não é um palindromo.
if var_global in nome:
    print('Verdadeiro.')
else:
    print('Não é um palindromo.')