class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer (self):
        print('Nhom nhom', self.nome)

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        super().__init__(nome, dono)
        self.raca = raca

    def miar(self):
        print('MIAU PORA')    
        
class Cachorro(Animal):
    def latir(self):
        print('AU AU PU')

gato = Gato('bilbo baggins', 'Camila', 'SRD')
cachorro = Cachorro('gandalf', 'Thales')
animal = Animal('toddy', 'gabriel')

print(gato.nome)
print(gato.dono)
gato.miar()
