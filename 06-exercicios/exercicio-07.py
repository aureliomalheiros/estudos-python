'''
Faça um programa que receba uma data de nascimento (15/07/87) e imprima

'Você nasceu em <dia> de <mês> de <ano>'
'''
data_de_nascimento = input('Data de nascimento: ')
dia, mes, ano = data_de_nascimento.split('/')
print(f'Você nasceu em {dia} do {mes} em {ano}')