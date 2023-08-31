class item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_valor(self):
        return self.preco

class Produto (item):
    def __init__(self, nome, preco, quant):
        self.quant = quant
        super().__init__( nome, preco)

    def calcular_valor(self):
        return self.preco * self.quant

class serviço(item):
    def __init__(self, nome, preco, horas):
        self.horas = horas
        super().__init__( nome, preco)
    def calcular_valor(self):
        return self.preco * self.horas

item1 = Produto("Shampoo", 45.00, 109)
print(item1.calcular_valor())
item2 = serviço("Estoque", 1000, 12)
print(item2.calcular_valor())
