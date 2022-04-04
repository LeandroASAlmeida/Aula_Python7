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
                                  '3- Conta Poupança\n'
                                  '4- Todas'))
    while (not tipoConta in [1,2,3,4]):
        print('Opção inválida!')
        AguardaLimpa
        tipoConta = int(input('Informe o tipo da conta desejada: \n'
                                    '1- Conta Corrente\n' + 
                                    '2- Conta Salário\n' 
                                    '3- Conta Poupança\n'
                                    '4- Todas'))
    return tipoConta

def menuOperacoes(pTipoConta):
    opcao = 0
    AguardaLimpa()
    print('Operação desejada: \n')
    match pTipoConta:
        case 1, 2:
            while (not (opcao in [1, 2, 3, 4, 5])):
                print('Opção inválida!')
            return int(input('1 - Sacar | 2 - Depositar | 3 - Transferir | 4 - Ver Saldo | 5 - Voltar \n'))
        case 3:
            while (not (opcao in [1, 2, 3])):
                print('Opção inválida!')
            return int(input('1 - Sacar | 2 - Ver Saldo | 3 - Voltar \n'))
        case default:
            pass