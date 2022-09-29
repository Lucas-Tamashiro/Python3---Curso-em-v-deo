# Le qualquer coisa do teclado e mostra no console suas propriedades

entrada = input('Digite algo a ser analisado: ')

print('Tipo: {}' .format(entrada, type(entrada)))

print('{} e um valor DECIMAL: {}' .format(entrada, entrada.isdecimal))

print('{} e um valor ALPHA NUMERICO: {}' .format(entrada, entrada.isalnum))

print('{} e um valor ALPHA: {}' .format(entrada, entrada.isalpha))

print('{} e um valor INTEIRO: {}' .format(entrada, entrada.isnumeric))
    
print('{} esta em MAIUSCULO: {}' .format(entrada, entrada.isupper))

