class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        ...

class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} emite latido"
    
class Gato(Animal):
    def falar(self):
        return f"{self.nome} emite mia"

huck = Cachorro("Huck")
fred = Gato("Fred")

print(huck.falar())
print(fred.falar())