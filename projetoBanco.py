from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from contaSalario import ContaSalario
import funcoes as f
import constantes as cons


contasC = {} #Conta Corrente
contasP = {} #Conta Poupança
contasS = {} #Conta Salário

opcao = 0
tipoConta = 0

f.LimpaTela()

while opcao != 5:
    print('Banco Proway\n'
          '1- Criar Conta\n'
          '2- Listar Contas\n'
          '3- Excluir Conta\n'
          '4- Operações\n'
          '5- Sair')
    opcao = int(input('Informe a opção desejada: \n'))
    f.LimpaTela()

    match opcao:
        case 1:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input(cons.MSG_CONTA_CADASTRAR)
            if (not f.validaTamanhoConta(numero)):
                f.AguardaLimpa()
            else:
                match tipoConta:
                    case 1:
                        if not(f.existeConta(numero, contasC, True)):
                            c = ContaCorrente(numero)
                            contasC[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)
                            del(c)
                    case 2:
                        if not(f.existeConta(numero, contasP, True)):
                            c = ContaPoupanca(numero)
                            contasP[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)
                            del(c)
                    case default:
                        if not(f.existeConta(numero, contasS, True)):
                            c = ContaSalario(numero)
                            contasS[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADATRAR)                            
                            del(c)
            f.AguardaLimpa()
        case 2:
            tipoConta = f.validaTipoConta(True)
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if (f.existeContaCadastrada(contasC, tipoConta)):
                        print(contasC)
                case 2:
                    if (f.existeContaCadastrada(contasP, tipoConta)):
                        print(contasP) 
                case 3:
                    if (f.existeContaCadastrada(contasS, tipoConta)):
                        print(contasS)
                case default:
                    print('Contas Correntes: ')
                    print(contasC)
                    print('Contas poupanças: ')
                    print(contasP)
                    print('Contas salário: ')
                    print(contasS)
            f.AguardaLimpa()
        case 3:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if f.existeContaCadastrada(contasC, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasC):
                                c = ContaCorrente(numero)
                                contasC.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case 2:
                    if f.existeContaCadastrada(contasP, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasP):
                                c = ContaPoupanca(numero)
                                contasP.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case default:
                    if f.existeContaCadastrada(contasS, tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR + '\n')
                        if f.validaTamanhoConta(numero):
                            if f.existeConta(numero, contasS):
                                c = ContaSalario(numero)
                                contasS.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
            f.AguardaLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            match tipoConta:
                case 1:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            valor = int(input(cons.MSG_VALOR_SAQUE))
                        case 2:
                            valor = int(input(cons.MSG_VALOR_DEPOSITO))
                        case 3:
                            valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasC):
                                    print(contasC[numero])
                        case default:
                            break
                case 2:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            valor = int(input(cons.MSG_VALOR_SAQUE))
                        case 2:
                            valor = int(input(cons.MSG_VALOR_DEPOSITO))
                        case 3:
                            valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasP):
                                    print(contasP[numero])
                        case default:
                            break
                case default:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            pass
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.validaTamanhoConta(numero):
                                if f.existeConta(numero, contasS):
                                    print(contasS[numero])
                        case default:
                            pass
        case 5:
            print(cons.MSG_EXIT_SISTEMA)
            f.AguardaLimpa()
            break
        case default:
            print(cons.MSG_OPCAO_INVALIDA)
            f.AguardaLimpa()