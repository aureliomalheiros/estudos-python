from random import randint
class Pessoa():
    #AnoAtual é um atributo de classe
    AnoAtual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #get_nascimento -> Atributos relacionados a instância
    def get_nascimento(self):
        print(self.AnoAtual - self.idade)

    #por_ano_nascimento -> Atributos relacionados a classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.AnoAtual - ano_nascimento
        return cls(nome, idade)
    @staticmethod
    def gerar_id():
        rand = randint(10, 1000)
        return rand


pessoa1 = Pessoa('Aurelio', 28)
pessoa2 = Pessoa.por_ano_nascimento('Ana', 24)
print(pessoa2.idade)
print(Pessoa.gerar_id())
print(Pessoa.gerar_id())
pessoa1.get_nascimento()

print(Pessoa.AnoAtual)