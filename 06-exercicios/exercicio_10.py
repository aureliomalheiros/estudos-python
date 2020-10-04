'''
Faça um programa que itere em uma string e toda vez que uma vogal aparecer na sua string print o seu nome
entre as letras.
string = bananas
b
eduardo
n
eduardo
n
eduardo
.
.
.
'''

palavra = 'aurelio'
vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        print(letra)
        print('Aurelio')
        print(letra)
    else:
        print('Vixi! Aí não tem vogal!')