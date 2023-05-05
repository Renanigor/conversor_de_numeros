def octal_para_binario():
    
    #VARIÁVEIS DE ENTRADA
    numero_octal = input('Digite um número octal: ')
    numero_octal_original = numero_octal
    numero_binario = []
    numero_final = ''

    # VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['8', '9']
    for numero in numeros_invalidos:
        if numero in str(numero_octal):
            print('Número inválido')
            return

    numero_decimal = int(numero_octal, 8)

    while numero_decimal > 0:
        resto = numero_decimal % 2
        numero_decimal = numero_decimal // 2
        numero_binario.append(resto)

    #MONTAGEM DE STRING
    for bit in reversed(numero_binario):
        numero_final += str(bit)

    print(f'O número octal: {numero_octal_original}, em binário é: {numero_final}')
    
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

    #FORMA A STRING FINAL
    for bit in reversed(numero_binario):
        numero_final += str(bit)
    
    print(f'O número decimal: {decimal_original}, em binário é: {numero_final}')

def hexadecimal_para_binario():
    
    #VARIÁVEIS DE ENTRADA
    numero_hexadecimal = input('Digite um número hexadecimal: ')
    numero_octal_original = numero_hexadecimal
    numero_binario = []
    numero_final = ''

    # VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['8', '9']
    for numero in numeros_invalidos:
        if numero in str(numero_hexadecimal):
            print('Número inválido')
            return

    numero_decimal = int(numero_hexadecimal, 16)

    while numero_decimal > 0:
        resto = numero_decimal % 2
        numero_decimal = numero_decimal // 2
        numero_binario.append(resto)

    #MONTAGEM DE STRING
    for bit in reversed(numero_binario):
        numero_final += str(bit)

    print(f'O número hexadecimal: {numero_octal_original}, em binário é: {numero_final}')