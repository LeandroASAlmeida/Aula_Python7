
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from contaSalario import ContaSalario
import funcoes as f

contasC = [] #Conta Corrente
contasS = [] #Conta Salário
contasP = [] #Conta Poupança

op = 0
tipoConta = 0

f.LimpaTela()
while op != 4:
    print('Banco Proway\n'
          '1- Criar Conta\n'
          '2- Listar Contas\n'
          '3- Excluir Conta\n'
          '4- Sair')

    op = int(input('Informe a opção desejada'))
    f.LimpaTela()
    match op:
        case 1:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input('Informe o número da conta: ')
            if len(numero) != 5:
                print('Número inválido')
                f.AguardaLimpa()
            else:
                match tipoConta:
                    case 1:   # CRIANDO DADOS DA CONTA CORRENTE /SALARIO / POUPANÇA                
                        if numero in contasC:
                            print('Conta Corrente já existente')
                            f.AguardaLimpa()
                        else:
                            contasC.append(numero)
                            print('Conta Corrente cadastrada com sucesso')
                            f.AguardaLimpa()
                    case 2:
                        if numero in contasS:
                            print('Conta Salário já existente')    
                            f.AguardaLimpa()
                        else:
                            contasS.append(numero)
                            print('Conta Salário cadastrada com sucesso')  
                            f.AguardaLimpa()
                    case outrocaso:
                        if numero in contasP:
                            print('Conta Poupança já existente')  
                            contasP.append(numero)
                            print('Conta Poupança cadastrada com sucesso')
            f.AguardaLimpa()     
        case 2:  # LISTANDO DADOS CONTA CORRENTE / SALARIO / POUPANÇA                  
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if  len(contasC) == 0:
                     print('Não há contas correntes cadastradas')
                    else:
                     print(contasC)
                case 2:
                    if len(contasS) == 0:
                     print('Não há contas salário cadastradas')
                    else:
                     print(contasS)
                case outrocaso:
                    if len(contasP) == 0:
                     print('Não há contas poupança cadastradas')
                    else:
                     print(contasP)
            f.AguardaLimpa()