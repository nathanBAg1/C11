
numero = input('Insira um número entre 1000 e 9999: ')

while int(numero) < 1000 or int(numero) > 9999:
    print('Número inválido!')
    numero = input('Insira um número entre 1000 e 9999: ')

print('Número da Unidade:', numero[3])
print('Número da Dezena:', numero[2])
print('Número da Centena:', numero[1])
print('Número do Milhar:', numero[0])