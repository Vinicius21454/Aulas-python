class ContaBancária():
    def __init__(self, numerodaconta, nome, saldo):
        self.numuerodaconta = numerodaconta
        self.nome = nome
        self.saldo = saldo

    def extrato(self):
        print(f"Oi, o seu saldo é R$". format(self.nome, self.saldo))

    def deposito(self, deposito):
        self.saldo = deposito + self.saldo
        print(f"O seu novo saldo é". format(self.saldo))

    def saque(self, saque):
        self.saldo = self.saldo - saque
        print(f"O total do seu saque é". format(self.saldo)) 

if __name__ == "__main__":
  numerodaconta = input("Digite o numero da sua conta")
  nome = input("Digite o seu nome")
  saldo = float(input("Digite o seu saldo"))

conta = ContaBancária(numerodaconta, nome, saldo)
conta.extrato()

deposito = float(input("Digite o seu deposito"))
conta.deposito(deposito)

saque = float(input("Digite seu saque "))
conta.saque(saque)
