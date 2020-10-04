'''
Faça um progama que peça 2 números inteiros e um número float. Calcule e mostre
    > O produto do dobro do primeiro com metade do segundo
    > A soma do triplo do primeiro com o terceiro
    > O terceiro elevado ao cubo
'''
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = float(input("Terceiro numero: "))

primeiraOP = n1*2*(n2/2)
segundaOP = n1*3+n3
terceiraOP = n3**3

print(f'\nPrimeira operação: {primeiraOP}\nSegunda operação: {segundaOP}\nTerceira operação: {terceiraOP}')