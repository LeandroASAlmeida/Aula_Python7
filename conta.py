import constantes as c #Alias "c"

class Conta(): # metodo construtor
    def __init__(self,conta):
        self.conta= conta
        self.saldo = 0 #iniciando a conta com saldo 0

    def verSaldo(self): # todos vão ter a função ver saldo
        return f'Saldo Atual:{self.saldo:,.2f}'   # "f " formatar string sem necessidade de concatenar.

    def sacar(self,valor,CCorrente = False):
        if valor > self.saldo:
           valor = valor
           return c.MSG_SALDO_INSUFICIENTE
        try:
            if CCorrente:
                 if valor + ( valor * 0.05) > self.saldo:
                      return c.MSG_SALDO_INSUFICIENTE
                 self.saldo -= valor
            else:
                if valor > self.saldo:
                    return  c.MSG_SALDO_INSUFICIENTE
                self.saldo -= valor
            return c.MSG_SUCESSO_SAQUE
        except:
            return c.MSG_ERRO_SAQUE