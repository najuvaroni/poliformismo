class profissao:
    def acao(self):
        return 'A principal atividade é: '
class estudante(profissao):
    def acao(self):
        print(super().acao(), 'estudar')

aluno1 = estudante()
aluno1.acao()