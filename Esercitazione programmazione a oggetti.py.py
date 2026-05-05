from abc import ABC, abstractmethod

# Classe astratta (ASTRAZIONE)
class Animale(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.__energia = 100   # INCAPSULAMENTO (attributo "privato")

    def mangia(self):
        self.__energia += 10

    def get_energia(self):   # metodo per accedere al dato
        return self.__energia

    @abstractmethod
    def verso(self):
        pass


# EREDITARIETA
class Cane(Animale):
    def verso(self):
        print(self.nome + " dice Bau")


class Gatto(Animale):
    def verso(self):
        print(self.nome + " dice Miao")


# OGGETTI
cane1 = Cane("Fido")
gatto1 = Gatto("Micia")

# uso dei metodi
cane1.mangia()
print(cane1.get_energia())

# POLIMORFISMO
animali = [cane1, gatto1]

for a in animali:
    a.verso()