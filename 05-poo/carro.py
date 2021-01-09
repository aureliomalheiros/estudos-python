class Carro():
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano =  ano
    def get_descricao(self):
        nome_longo = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_longo.title()

meu_novo_carro = Carro('audi', 'a4', 2019)
print(meu_novo_carro.get_descricao())