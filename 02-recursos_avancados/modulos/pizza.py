def fazer_pizza(tamanho, *tipos):
    print(f'Tamanho: {tamanho}')
    for tipo in tipos:
        print(f'- {tipo}')