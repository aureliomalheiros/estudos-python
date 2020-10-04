'''
Estruturas de decisão

if
elif
else
'''

'''
resposta= input('Deseja instalar o programa? y/n ')

if resposta.lower() == 'y':
    print('Vamos instalar!!!')
elif resposta.lower() == 'n':
    print('Não vamos instalar!')
else:
    print('Você digitou algo errado!')
    print('digite y ou n')
'''
#Comprar algo
conta_bancaria = float(input('Conta bancaria: '))
produto = input('Qual o produto: ')
valor = float(input('Valor: '))
necessidade = input('Tá precisando? [s/n]')



if conta_bancaria >= valor and necessidade == 's':
    print(f'Posso comprar essa parada({produto})!!!')
elif conta_bancaria >= valor and necessidade == 'n':
    print('Não preciso comprar agora!')
else:
    print('Não vai rolar! :(')