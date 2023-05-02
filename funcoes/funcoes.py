from funcoes.para_decimal import binario_para_decimal, octal_para_decimal
from funcoes.para_binario import decimal_para_binario

#ESCOLHER A OPERAÇÃO DE CONVERSÃO
def escolher():
    print('Digite [1] DECIMAL -> BINÁRIO, [2] BINÁRIO -> DECIMAL, [3] OCTAL -> DECIMAL')
    escolha = input('Digite sua opção: ').strip()
    if escolha == '1':
        decimal_para_binario()
    elif escolha == '2':
        binario_para_decimal()
    elif escolha == '3':
        octal_para_decimal()
    else:
        print('Digite uma opção válida.')


