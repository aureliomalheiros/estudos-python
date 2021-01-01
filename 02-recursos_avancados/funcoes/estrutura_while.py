def get_nome(nome, sobrenome):
    nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()


while True:
    print('\nDigite seu nome!')
    print("(Pressione 'q' para sair!)")
    primeiro_nome = input('Primeiro nome: ')
    if primeiro_nome == 'q':
        break
    segundo_nome = input('Segundo nome: ')
    if segundo_nome == 'q':
        break
    nome = get_nome(primeiro_nome, segundo_nome)
    print(f'\nOlá {nome}')
