from conta import Conta


class ContaCorrente (Conta):
    limite = 0.0
     
    def __init__ (self, x, n, s):
        self.numero = x
        self.nome = n
        self.saldo = s

         
    def depositar (self, q):
        desconto = 0.0035 * q
        self.saldo += (q - desconto)
         
    def sacar (self, q):
        desconto = 0.0035 * q
        if (self.saldo + self.limite) >= (q + desconto):
            self.saldo -= (q + desconto)
            return True
        else:
            print ("Saldo insuficiente.")
            return False
             
    def atualizar (self, taxa):
        self.saldo += (2 * self.saldo * taxa)
         
    def noVermelho (self, taxa):
        self.saldo += (self.saldo * taxa)
         
    def imprimeSaldo (self):
        print ("Conta Corrente.")
        print ("Cliente:", self.nome)
        print ("Saldo: %.5f" % (self.saldo))
    
    