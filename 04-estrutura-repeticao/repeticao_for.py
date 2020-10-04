"""
for elemento in interavel
    faça algo

Para cada 'elemento' dentro do 'iteravel'
    faça algo
"""

nome = "Tribix"

for posicao,letra in enumerate(nome):
    print(f'{posicao} - {letra}')

frase = 'Vamos fazer um teste!'.split()

for separa in frase:
    print(separa)