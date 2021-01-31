arquivo = '/home/tribix/estudos/programacao/python/estudos-python/02-recursos_avancados/manipulando-arquivos/escrita.txt'
with open(arquivo, 'w') as arquivo:
    arquivo.write("Estou estudando python")
    arquivo.write("\nTeste de linha")