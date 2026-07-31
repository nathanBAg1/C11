
numero = int(input('Insira um número: '))

inferior = int(input('Insira o limite inferior do intervalo: '))
superior = int(input('Insira o limite superior do intervalo: '))

print('Tabuada: ')
for c in range(inferior, superior+1):
    print(numero * c)