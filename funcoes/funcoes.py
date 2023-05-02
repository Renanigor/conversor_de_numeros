from funcoes.para_binario import octal_para_binario, decimal_para_binario
from funcoes.para_decimal import binario_para_decimal, octal_para_decimal


def escolha():
    
    print('De qual sistema você quer converter? \n [1] BINÁRIO \n [2] OCTAL \n [3] DECIMAL \n [4] HEXADECIMAL')
    
    escolha = input('Digite o sistema desejado: ')
    opcao = {'1': de_binario, '2': de_octal, '3': de_decimal, '4': de_hexadecimal}
    
    if escolha in opcao:
        if callable(opcao[escolha]):
            return opcao[escolha]()
        else:
            print(opcao[escolha])
    else:
        print('Digite um número de sistema válido.')
    return

#PARA QUAL SISTEMA
def de_binario():
    
    print('Para qual sistema você quer converter? \n [1] OCTAL \n [2] DECIMAL \n [3] HEXADECIMAL')
    
    escolha = input('Digite uma opção: ').strip()
    opcao = {'1': 'AINDA ESTAMOS TRABALHANDO NISSO!', '2': binario_para_decimal, '3': 'AINDA ESTAMOS TRABALHANDO NISSO!', '4': 'AINDA ESTAMOS TRABALHANDO NISSO!' }
    
    if escolha in opcao:
        if callable(opcao[escolha]):
            return opcao[escolha]()
        else:
            print(opcao[escolha])
    else:
        print('Digite um número de sistema válido.')

    return

def de_octal():
    
    print('Para qual sistema você quer converter? \n [1] BINARIO \n [2] DECIMAL \n [3] HEXADECIMAL')

    escolha = input('Digite uma opção: ').strip()
    opcao = {'1': octal_para_binario, '2': octal_para_decimal, '3': 'AINDA ESTAMOS TRABALHANDO NISSO!', '4': 'AINDA ESTAMOS TRABALHANDO NISSO!' }

    if escolha in opcao:
        if callable(opcao[escolha]):
            return opcao[escolha]()
        else:
            print(opcao[escolha])
    else:
        print('Digite um número de sistema válido.')

    return

def de_decimal():
    
    print('Para qual sistema você quer converter? \n [1] BINARIO \n [2] OCTAL \n [3] HEXADECIMAL')

    escolha = input('Digite uma opção: ').strip()
    opcao = {'1': decimal_para_binario, '2': 'AINDA ESTAMOS TRABALHANDO NISSO!', '3': 'AINDA ESTAMOS TRABALHANDO NISSO!', '4': 'AINDA ESTAMOS TRABALHANDO NISSO!' }

    if escolha in opcao:
        if callable(opcao[escolha]):
            return opcao[escolha]()
        else:
            print(opcao[escolha])
    else:
        print('Digite um número de sistema válido.')

    return
    
def de_hexadecimal():
    return