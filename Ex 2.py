#ex2 Aqui é utilizado um método para criar a uma lista e, junto a ele, outro método para criação de uma chave de dicionário, a qual removerá todos os caracteres duplicados. Após isso, é feito o print com as aspas vazias para poder utilizar o método join, o qual irá realizar a junção de todos os caracteres do dicionário e imprimi-lo corretamente
frase2 = input('Digite aqui a frase da qual deseja remover as letras duplicadas: ')
l2 = list(dict.fromkeys(frase2))
print(''.join(l2))

