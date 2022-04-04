from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from contaSalario import ContaSalario
import funcoes as f

contasC = {} #Conta Corrente
contasP = {} #Conta Poupança
contasS = {} #Conta Salário

opcao = 0
tipoConta = 0

f.LimpaTela()

while opcao != 5:
    print('Banco PROWAY')
    print('1 - Criar Conta | 2 - Listar Contas | 3 - Excluir Contas | 4 - Operações | 5 - Sair')
    opcao = int(input('Informe a opção desejada!'))
    f.LimpaTela()

    match opcao:
        case 1:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input('Informe o número da conta!')
            if len(numero) != 5:
                print('Número inválido!')
                f.AguardaLimpa()
            else:
                match tipoConta:
                    case 1:
                        if numero in contasC:
                            print('Conta corrente já existente!')
                        else:
                            c = ContaCorrente(numero)
                            contasC[c.numeroConta] = 0
                            print('Conta corrente cadastrada com sucesso')
                            del(c)
                    case 2:
                        if numero in contasP:
                            print('Conta poupança já existente!')
                        else:
                            c = ContaPoupanca(numero)
                            contasP[c.numeroConta] = 0
                            print('Conta poupança cadastrada com sucesso')
                            del(c)
                    case default:
                        if numero in contasS:
                            print('Conta salário já existente!')
                        else:
                            c = ContaSalario(numero)
                            contasS[c.numeroConta] = 0
                            print('Conta salário cadastrada com sucesso')
                            del(c)
            f.AguardaLimpa()
        case 2:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas correntes cadastradas')
                    else:
                        print(contasC)
                case 2:
                    if len(contasP) == 0:
                        print('Não há contas salários cadastradas')
                    else:
                        print(contasP) 
                case 3:
                    if len(contasS) == 0:
                        print('Não há contas poupanças cadastradas')
                    else:
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
                    if len(contasC) == 0:
                        print('Não há contas correntes cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if not numero in contasC:
                                print('Conta inexistente!')
                            else:
                                c = ContaCorrente(numero)
                                contasC.pop(c.numeroConta)
                                print('Conta excluída com sucesso!')
                                del(c)
                case 2:
                    if len(contasP) == 0:
                        print('Não há contas poupança cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if not numero in contasP:
                                print('Conta inexistente!')
                            else:
                                c = ContaPoupanca(numero)
                                contasP.pop(c.numeroConta)
                                print('Conta excluída com sucesso!')
                                del(c)
                case default:
                    if len(contasS) == 0:
                        print('Não há contas poupanças cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: \n')
                        if len(numero) != 5:
                            print('Número inválido!')
                        else:
                            if numero in contasS:
                                print('Conta inexistente')
                            else:
                                c = ContaSalario(numero)
                                contasS.pop(c.numeroConta)
                                print('Conta excluída com sucesso!')
                                del(c)
            f.AguardaLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            match tipoConta:
                case 1,2:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            pass
                        case default:
                            break
                case default:
                    opcao = f.menuOperacoes(tipoConta)
                    match opcao:
                        case 1:
                            pass
                        case 2:
                            pass
                        case default:
                            pass
        case 5:
            print('Obrigado por usar o sistema!')
            f.AguardaLimpa()
            break
        case default:
            print('Opção inválida!')
            f.AguardaLimpa()