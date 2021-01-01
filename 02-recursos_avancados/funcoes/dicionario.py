def compilando_pessoa(primeiro_nome, segundo_nome, idade='', profissao=''):
    pessoa = {'nome': primeiro_nome, 'sobrenome': segundo_nome}

    if idade:
        pessoa['idade'] = idade
    
    if profissao:
        pessoa['profissao'] = profissao
    
    return pessoa

identificacao = compilando_pessoa('Jimi', 'Hendrix', idade=27, profissao='Musico')

print(identificacao)