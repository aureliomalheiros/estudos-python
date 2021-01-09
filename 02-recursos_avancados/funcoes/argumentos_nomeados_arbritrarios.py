def get_perfil(nome, sobrenome, **info_usuarios):
    perfil = {}
    perfil['Primeiro_Nome'] = nome
    perfil['Segundo_Nome'] = sobrenome
    for chave, valor in info_usuarios.items():
        perfil[chave] = valor
    return perfil
perfil_usuario = get_perfil('Albert', 'einstein', localizacao='princeton', profissao='fisico')
print(perfil_usuario)