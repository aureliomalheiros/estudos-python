def quadrado(lista_de_numeros):
    lista_de_reposta = []
    for numero in lista_de_numeros:
        lista_de_numeros.append(numero**2)
    
    return lista_de_reposta


def cubica(lista_de_numeros):
    lista_de_reposta = []
    for numero in lista_de_numeros:
        lista_de_numeros.append(numero**3)
    return lista_de_reposta

lista_de_valores = []


for valor in range(10):
    lista_de_valores.append(int(input('Digite os valores: ')))

dicionario = {
    'lista_padrao': lista_de_valores,
    'lista_quadrada': quadrado(lista_de_valores),
    'lista_cubica': cubica(lista_de_valores)
}

print(dicionario)