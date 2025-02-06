class Aluno():
    def __init__(self, nome, matricula,notas,):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas 

    def media(self):
      soma = sum(self.notas)
      quantidade = len(self.notas) 
      media = soma / quantidade

      return media

    def verificar_situacao(self):
       if self.media() >= 5.0:
          print("Aprovado")
       else:
          print("Reprovado")

if __name__ == "__main__":
   nome = input("Digite seu nome:")
   matricula = input("Digite a sua matrícula:")
   

   notas = []     
   for i in range(5):
      nota = float(input("Digite a sua nota:"))
      notas.append(nota)

   vinicius = Aluno(nome, matricula, notas)
   Aluno.media()

   media = float(input("Digite um numero"))
   Aluno