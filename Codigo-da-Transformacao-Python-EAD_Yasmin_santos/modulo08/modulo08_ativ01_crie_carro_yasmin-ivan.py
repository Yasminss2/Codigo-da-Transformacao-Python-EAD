class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"marca: {self.marca}, modelo: {self.modelo}"

meu_carro = Carro("renault", "clio")
print(meu_carro.exibir_info())