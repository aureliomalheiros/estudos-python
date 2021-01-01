def get_nome_completo(nome, ultimo_nome, segundo_nome=''):
    if segundo_nome:
        nome_completo = nome + ' ' + segundo_nome + ' ' + ultimo_nome
    else:
        nome_completo = nome + ultimo_nome
    return nome_completo

Nome = get_nome_completo('Jimi', 'Hendrix')
print(Nome)

Nome = get_nome_completo('Mr', 'Jimi', 'Hendrix')
print(Nome)