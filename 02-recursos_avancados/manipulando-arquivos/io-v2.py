arquivo = open('pessoas.csv')
#Uso de streaming
#Faz a leitura do arquivo de acordo com a demanda
for registro in arquivo:

    print('Nome: {}, Idade {}' .format(*registro.split(',')))

arquivo.close()
