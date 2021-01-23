class Carro():
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano =  ano
    def get_descricao(self):
        nome_longo = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_longo.title()

class Baterry():
    def __init__(self, bateria=70):
        self.bateria = bateria
    def descricao_bateria(self):
        print("A bateria tem " + str(self.bateria) + "-KWh bateria")
#Herança da classe carro 
#Dessa forma criamos a classe filha

class Carro_Eletrico(Carro):
    def __init__(self, fabricante, modelo, ano):
        #Função super é utilizada para criar um conexão entre a classe filha e a pai.
        #Chame o método __init__()
        super().__init__(fabricante, modelo, ano)
        self.bateria = Baterry()

meu_tesla = Carro_Eletrico('Tesla', 'Model S', 2016)
print(meu_tesla.get_descricao())
meu_tesla.bateria.descricao_bateria()

meu_novo_carro = Carro('audi', 'a4', 2019)
print(meu_novo_carro.get_descricao())