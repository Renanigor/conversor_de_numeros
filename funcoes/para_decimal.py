def binario_para_decimal():
   
    numero_binario = input('Digite um número binário: ')

    #VARIÁVEIS
    tamanho_potencia = len(numero_binario)
    i = 0
    j = tamanho_potencia - 1
    soma = 0
    
    #VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['2', '3', '4', '5', '6', '7', '8', '9']
    for numero in numeros_invalidos:
        if numero in str(numero_binario):
            print('Número inválido')
            return
        
    #CONVERSÃO DO NÚMERO
    for bit in numero_binario:
        multiplicacao = 2**j * int(bit)
        soma += multiplicacao
        i += 1
        j -= 1

    print(f'o número binário: {numero_binario}, em decimal é: {soma}')


def octal_para_decimal():
    
    numero_octal_original = input('Digite um número octal: ')
    numero_octal = list(numero_octal_original)

    #VARIÁVEIS
    tamanho_potencia = len(numero_octal)
    i = 0
    j = tamanho_potencia - 1
    soma = 0

    # VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['8', '9']
    for numero in numeros_invalidos:
        if numero in str(numero_octal):
            print('Número inválido')
            return
        
    #CONVERSÃO DO NÚMERO
    for numero in numero_octal:
        resultado = int(numero) * (8**j)
        soma += resultado
        i += 1
        j -= 1
    print(f'o número octal: {numero_octal_original}, em decimal é: {soma}')

def hexadecimal_para_decimal():
    
    numero_hexadecimal_original = input('Digite um número hexadecimal: ')
    numero_hexadecimal = list(numero_hexadecimal_original)

    #VARIÁVEIS
    tamanho_potencia = len(numero_hexadecimal)
    i = 0
    j = tamanho_potencia - 1
    soma = 0

    #CONVERSÃO DO NÚMERO
    for numero in numero_hexadecimal:
        resultado = int(numero, 16) * (16**j)
        soma += resultado
        i += 1
        j -= 1

    print(f'o número hexadecimal: {numero_hexadecimal_original}, em decimal é: {soma}')
