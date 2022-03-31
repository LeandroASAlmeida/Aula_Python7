import os
import time

def LimpaTela():    #Limpar a tela
    os.system('cls')

def Aguarda():
    time.sleep(5)   # demora tantos segundos para limpar

def AguardaLimpa():
    Aguarda()
    LimpaTela()

def validaTipoConta():
    tipoConta = 0
    tipoConta = int(input('Informe o tipo da conta desejada: \n'
                                  '1- Conta Corrente\n' + 
                                  '2- Conta Salário\n' 
                                  '3- Conta Poupança\n'))
    while (not tipoConta in [1,2,3]):
        print('Opção inválida!')
        AguardaLimpa
        tipoConta = int(input('Informe o tipo da conta desejada: \n'
                                    '1- Conta Corrente\n' + 
                                    '2- Conta Salário\n' 
                                    '3- Conta Poupança\n'))
    return tipoConta
