
class Mamifero():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.parado = True
        
    def mover(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e esta se movendo')
        self.parado = False

    def parar(self):
        print(self.nome + ' é ' +__class__.__name__ +' e esta parado')
        self .parado = True
        
    def comer(self):
        print(self.nome + ' é ' +__class__.__name__ +' e esta comendo')
        

class Cao(Mamifero):
    def __init__(self,nome):
        self.nome = nome

    def latir(self):
        print(self.nome + ' é ' +__class__.__name__ +' e esta latindo')

class Pessoa(Mamifero):
    def falar(self):
        print(self.nome + ' é ' +__class__.__name__ +' e esta falando')
   

pessoa = Pessoa('Leandro', 33)
pessoa.falar()


