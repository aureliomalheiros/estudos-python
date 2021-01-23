import Carro
#Herança da classe carro 
#Dessa forma criamos a classe filha

class Carro_Eletrico(Carro):
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)

meu_tesla = Carro_Eletrico('Tesla', 'Model S', 2016)
print(meu_tesla.get_descricao())