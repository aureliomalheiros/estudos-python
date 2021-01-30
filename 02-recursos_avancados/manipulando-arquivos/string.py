arquivo = 'numeros.txt'

with open(arquivo) as dados:
    linhas = dados.readlines()
#armazena os digitos
string = ''
for linha in linhas:
    string += linha.rstrip()
print(string)
print(len(string))