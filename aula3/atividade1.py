import math
class Circulo:
    def __init__(self,raio,):
        self.raio = raio

    def calacular_area(self):
        return math.pi * (self.raio ** 2)
        
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    


if __name__ == "__main__":
    raio = float(input("Digite o raio do Circulo"))
    Circulo = Circulo(raio)

    area = Circulo.calacular_area()
    perimetro = Circulo.calcular_perimetro()

    print(area)
    print(perimetro)