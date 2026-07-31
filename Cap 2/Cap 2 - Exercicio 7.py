
palavra = input('Insira a Palavra: ')

for c in range(0, len(palavra)):
    print(palavra[c].upper())

print('Quantidade de vogais:',
      palavra.count('a') + palavra.count('e') + palavra.count('i') +
      palavra.count('o') + palavra.count('u') +
      palavra.count('A') + palavra.count('E') + palavra.count('I') +
      palavra.count('O') + palavra.count('U'))

if 'A' in palavra or 'a' in palavra:
    print('A letra "A" está presente nessa palavra!')
else:
    print('A letra "A" não está presente nessa palavra!')