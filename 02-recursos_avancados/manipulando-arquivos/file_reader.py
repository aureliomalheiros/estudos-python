arquivos = 'numeros.txt'
with open(arquivos) as numeros:
    for linha in numeros:
        print(linha.rstrip())