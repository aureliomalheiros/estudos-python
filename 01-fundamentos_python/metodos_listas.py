'''
append
insert
count
reverse
pop
remove
'''

lista_compras = []
res = ''

while res != 'acabou':
    res = input("O que tem que comprar? ")
    if res != 'acabou': 
        lista_compras.append(res)

print('*' * 10)
for numeracao,lista in enumerate(lista_compras):
    print(f'{numeracao}-{lista}')
print('*' * 10)
