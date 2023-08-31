class AnimalAquatico:
    def nadando(self):
        pass

class Peixe (AnimalAquatico):
    def nadando(self):
        print("o peixe está nadando...")

class Tartaruga (AnimalAquatico):
    def nadando(self):
        print("A tartaruga está nadando...")

animal1 = Tartaruga()
animal1.nadando()
