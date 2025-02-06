class Livro:
    def __init__(self, nome, autor, editor):
        self.nome_livro = nome
        self.autor = autor
        self.editor = editor
        self.emprestado = False

    def ler(self):
        print(f"O livro {self.nome_livro} esta sendo lido")

    def emprestar(self):
        if self.emprestado:
            self.emprestado = True

    def devolver(self):
        if self.emprestado:
            self.emprestado = False

    def __str__(self):
        if self.emprestado:
            return f"O livro {self.nome_livro}. escrito por {self.autor} esta emprestado"
        else:
            return f"O livro {self.nome_livro}, escrito por {self.autor} não esta emprestado" 

    def __eq__(self, outro_livro):
        if isinstance(outro-livro, Livro):
            return self.nome_livro == outro_livro.nome_livro
        return False


livro_vinicius = Livro("Estraordinário", "Resende", "Pedro")
livro_talita = Livro("Estraordinário2", "Resende2", "Pedro2")
livro_lucas = Livro("Estraordinário3", "Resende3", "Pedro3")

livro_vinicius.emprestar()