'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

produto1 = float(input('Valor do produto 1: '))
produto2 = float(input('Valor do produto 2: '))
produto3 = float(input('Valor do produto 3: '))

if produto1 < (produto2 and produto3):
    print(f'Compra o produto1, olha o preço {produto1}')
elif produto2 < (produto1 and produto3):
    print(f'Compra o produto2, olha o preço {produto2}')
elif produto3 < (produto1 and produto2):
    print(f'Compra o produto3, olha o preço {produto3}')
else:
    print("Você digitou algo errado!!!")
