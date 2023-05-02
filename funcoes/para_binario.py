from funcoes.para_decimal import binario_para_decimal, octal_para_decimal

def octal_para_binario():
    pass

def decimal_para_binario():
    
    #VARIÁVEIS
    numero_binario = []
    numero_final = ''
    decimal = int(input('Digite um número decimal: '))
    decimal_original = decimal

    while decimal > 0:
        resto = decimal % 2
        decimal = decimal // 2
        numero_binario.append(resto)
    
    numero_binario.reverse()

    #FORMA A STRING FINAL
    for bit in numero_binario:
        numero_final += str(bit)
    
    print(f'O número decimal: {decimal_original}, em binário é: {numero_final}')