class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0

meu = carro("fiat", "uno")
outro = carro("vw", "gol")
print(meu.marca, meu.modelo, meu.km)
print(outro.modelo)
print(type(meu), __name__)