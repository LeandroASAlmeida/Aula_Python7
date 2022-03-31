
class Conta(): # metodo construtor
    def __init__(self,conta):
        self.conta= conta
        self.saldo = 0 #iniciando a conta com saldo 0
    def verSaldo(self): # todos vão ter a função ver saldo
        return f'Saldo Atual:{self.saldo:,.2f}'   # "f " formatar string sem necessidade de concatenar.
