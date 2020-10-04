arquivo = open('pessoas.csv')
'''

Faz a leitura de todo o arquivo e armazena na variavel dados

'''
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade {}' .format(*registro.split(',')))
