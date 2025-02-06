class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
      
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    


if __name__ == "__main__":
    altura = float(input("Digite a altura do retangulo"))
    largura = float(input("Digite a largura"))


retangulo = Retangulo(largura, altura)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(area)
print(perimetro)



     
    