arquivo = '/home/tribix/estudos/programacao/python/estudos-python/02-recursos_avancados/manipulando-arquivos/convidados.txt'

fim = ''
with open(arquivo, 'w') as dados:
    while fim != 'sim':
        nome = input('Nome: ')
        dados.write(nome + '\n')
        fim = input('Deseja sair?(sim/qualquer tecla)')