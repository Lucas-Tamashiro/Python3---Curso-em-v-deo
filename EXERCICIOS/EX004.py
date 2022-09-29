# Todos os tipos de dados em PYTHON

varBool = bool(input('Digite algo para TRUE, deixe em branco para FALSE: '))

varInt = int(input('Digite um numero INTEIRO: '))

varFloat = float(input('Digite um numero REAL: '))

varStr = str(input('Digite um TEXTO: '))

print('{} {} {} {}'.format(type(varBool), type(varInt), type(varFloat), type(varStr)))

print('{} {} {} {}'.format(varBool, varInt, varFloat, varStr))