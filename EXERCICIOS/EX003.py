# coding=iso-8859-1

# soma entre dois números inteiros
# input recebe sempre em texto, necessário converter para int ao atribuir a variável para realizar a soma

n1, n2 = int(input('Digite o nº 1: ')), int(input('Digite o nº 2: '))

print('A soma entre os números {} e {} é igual a: {}' .format(n1, n2, n1 + n2))