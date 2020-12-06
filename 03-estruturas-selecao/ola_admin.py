usuarios = ['root', 'aurelio', 'nsa', 'admin', 'baby']

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print('Olá admin, gostaria de ver o seu relatório?')
        else:
            print('Bem vindo! ' + usuario)
else:
    print('Não tem usuários na sua lista')