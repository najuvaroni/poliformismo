class profissao:
    def acao(self):
        pass

class estudante(profissao):
    def acao(self):
        print("Estudando...")

aluno1 = estudante()
aluno1.acao()