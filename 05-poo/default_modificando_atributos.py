class Carro():
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.km = 0 #Atributo Default
    def get_descricao(self):
        descricao = str(self.ano) + ' ' + str(self.fabricante) + ' ' +  str(self.ano)
        return descricao
    def get_km(self):
        print("O carro tem: " + str(self.km) + ' Km')
    def update_km(self):
        if kms >= self.km:
            self.km = kms
        else:
            print("Atualização não pode ser feita")

meu_novo_carro = Carro('Chevrolet', 'Celta', '2012')
print(meu_novo_carro.get_descricao())
meu_novo_carro.get_km()

#Mudando Atributo default
meu_novo_carro.km = 22
meu_novo_carro.get_km()
