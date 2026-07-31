
distancia = int(input('Informe a distância da sua viagem: '))

if distancia <= 200:
    print('O preco da passagem será de R$', distancia * 0.50)
else:
    print('O preco da passagem será de R$', distancia * 0.45)