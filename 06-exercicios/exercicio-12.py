'''
Faça um programa que: Dada uma lista [1,2,3,4,5,6,7,8,9,10] e um número inteiro
imprima a tabuada desse número
'''
lista = [1,2,3,4,5,6,7,8,9,10]
numero = int(input("Digite um número: "))

print('*' * 20)
print('MULTIPLICAÇÃO')
print('*' * 20)
for item in lista:
    print(f'{item} x {numero} = {item*numero}')
print('*' * 20)
print('SUBTRAÇÃO')
print('*' * 20)
for item in lista:
    print(f'{item} - {numero} = {item - numero}')
print('*' * 20)
print('SOMA')
print('*' * 20)
for item in lista:
    print(f'{item} + {numero} = {item + numero}')
print('*' * 20)
print('DIVISAO')
print('*' * 20)
for item in lista:
    print(f'{item} : {numero} = {item / numero}')
