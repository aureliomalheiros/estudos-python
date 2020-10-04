'''
enpacotamento
'''
def empacotamente_argumento(argumento, *empacotamento):
    print(
        argumento,
        empacotamento)

def pacote_nomeado(argumento_nomeado = 'n tem nada', **pacote_nomeado):
    print(argumento_nomeado, pacote_nomeado)

print(empacotamente_argumento('Python',1,2,3))
