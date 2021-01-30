#Armazenando dados de arquivos dentro de variáveis
#readlines() -> armazena cada linha do arquivo em uma lista
arquivo = 'numeros.txt'

with open(arquivo) as numeros:
    linhas = numeros.readlines()
for linha in linhas:
    print(linha.rstrip())