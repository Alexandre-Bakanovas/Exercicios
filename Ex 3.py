#ex3: Primeiro é definido a função palindromo. Nela, será realizado alguns testes de validação para saber se a string digitada representa um palindrome ou não. Caso em sua composição haja alguns casos, ela automaticamente adiciona à lista palindromes.
def palindromo():
    tamanho = input('Digite uma palavra para verificar se ela possui palindromo: ')
    global var_global
    var_global = tamanho
    tamanho1 = len(tamanho)
    palindromos = []
    for x in range(2,tamanho1+1):
        min = 0
        maxi = x
        while maxi < tamanho1+1:
            testString = tamanho[min:maxi]
            if(len(testString)%2==0):
                meio = len(testString)//2
                if( testString[0:meio] == testString[meio:][::-1] ):
                    palindromos.append(testString)
            else:
                meio = len(testString)//2
                if(testString[0:meio] == testString[(meio+1):][::-1]):
                    palindromos.append(testString)
            min += 1
            maxi += 1
    return palindromos

print(palindromo())

