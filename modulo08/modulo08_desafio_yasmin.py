# Exemplo prático de Herança e Polimorfismo na Programação Orientada a Objetos (POO) em Python

class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, memoria_ram):
        super().__init__(marca, modelo)
        self.memoria = memoria_ram

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Memória RAM: {self.memoria} GB"

# Criando a instância com o seu celular
meu_celular = Smartphone("Motorola", "Moto G42", 4)
print(meu_celular.exibir_info())