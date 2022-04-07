import os
import time
import constantes as cons

def LimpaTela():
    os.system('cls')

def Aguarda():
    time.sleep(4)

def AguardaLimpa():
    Aguarda()
    LimpaTela()

def validaTipoConta(pListagem = False):
    tipoConta = 0
    if pListagem:
        tipoConta = int(input(cons.MSG_OPCOES_TIPOS_CONTAS_LISTAGEM))
    else:
        tipoConta = int(input(cons.MSG_OPCOES_TIPOS_CONTAS))
    while (not tipoConta in [1,2,3,4]):
        print(cons.MSG_OPCAO_INVALIDA)
        AguardaLimpa()
        if pListagem:
            tipoConta = int(input(cons.MSG_OPCOES_TIPOS_CONTAS_LISTAGEM))
        else:
            tipoConta = int(input(cons.MSG_OPCOES_TIPOS_CONTAS))
    return tipoConta

def menuOperacoes(pTipoConta):
    opcao = 0
    AguardaLimpa()
    print('Operação desejada: \n')
    match pTipoConta:
        case 1:
            print('1 - Sacar \n'
                  '2 - Depositar \n'
                  '3 - Transferir \n'
                  '4 - Ver Saldo \n'
                  '5 - Encerrar \n')
            opcao = int(input('Informe a opção desejada: \n'))
            while (not opcao in [1, 2, 3, 4, 5]):
                print(cons.MSG_OPCAO_INVALIDA)
                AguardaLimpa()
                print('1 - Sacar\n'
                    | '2 - Depositar\n'
                      '3 - Transferir\n'
                      '4 - Ver Saldo\n'
                      '5 - Encerrar \n')
                opcao = int(input('Informe a opção desejada: \n'))
            return opcao
        case 2:
            print('1 - Sacar\n'
                | '2 - Depositar\n'
                  '3 - Transferir\n'
                  '4 - Ver Saldo\n'
                  '5 - Encerrar \n')
            opcao = int(input('Informe a opção desejada: \n'))
            while (not opcao in [1, 2, 3, 4, 5]):
                print(cons.MSG_OPCAO_INVALIDA)
                AguardaLimpa()
                print('1 - Sacar\n'
                      '2 - Depositar\n'
                      '3 - Transferir\n'
                      '4 - Ver Saldo\n'
                      '5 - Encerrar \n')
                opcao = int(input('Informe a opção desejada!'))
            return opcao
        case 3:
            print('1 - Sacar | 2 - Ver Saldo | 3 - Encerrar \n')
            opcao = int(input('Informe a opção desejada: \n'))
            while (not opcao in [1, 2, 3]):
                print(cons.MSG_OPCAO_INVALIDA)
                AguardaLimpa()
                print('1 - Sacar | 2 - Ver Saldo | 3 - Encerrar \n')
                opcao = int(input('Informe a opção desejada: \n'))
            return opcao
        case default:
            pass

def validaTamanhoConta(pConta):
    if len(pConta) != cons.TAMANHO_VALIDO_CONTA:
        print(cons.MSG_ERRO_CONTA)
    return len(pConta) == cons.TAMANHO_VALIDO_CONTA

def existeConta(pNumero, pConta, pCadastroConta = True):
    if not pCadastroConta:
        if not pNumero in pConta:
            print(cons.MSG_CONTA_INEXISTENTE)
    else:
        if pNumero in pConta:
            print(cons.MSG_CONTA_EXISTENTE)
    return pNumero in pConta

def existeContaCadastrada(pConta, pTipoConta):
    if len(pConta) == 0:
        if pTipoConta == 1:
            print(cons.MSG_SEM_CONTA_CORRENTE)
        elif pTipoConta == 2:
            print(cons.MSG_SEM_CONTA_POUPANCA)
        else:
            print(cons.MSG_SEM_CONTA_SALARIO)
    return len(pConta) > 0
