from funcoes.para_decimal import binario_para_decimal, octal_para_decimal
from funcoes.para_binario import decimal_para_binario, octal_para_binario

#ESCOLHER A OPERAÇÃO DE CONVERSÃO
def escolher():
    print('De qual sistema você quer converter? \n [1] BINÁRIO -> DECIMAL \n [2] OCTAL -> DECIMAL \n [3] DECIMAL -> BINÁRIO \n [4] OCTAL -> BINÁRIO ')
    escolha = input('Digite sua opção: ').strip()
    
    if escolha == '1':
        binario_para_decimal()

    elif escolha == '2':
        octal_para_decimal()

    elif escolha == '3':
        decimal_para_binario()
    
    elif escolha == '4':
        octal_para_binario()

    else:
        print('Digite uma opção válida.')


