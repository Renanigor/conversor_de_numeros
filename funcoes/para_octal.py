def binario_para_octal():
   
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
        multiplicacao = 2**j *  int(bit)
        soma += multiplicacao
        i += 1
        j -= 1
    resultado_final = oct(soma)

    print(f'o número binário: {numero_binario}, em octal é: {resultado_final[2:]}')

def decimal_para_octal():
    
    numero_decimal = int(input('Digite um número decimal: '))

    numero_octal = oct(numero_decimal)
    
    print(f'o número decimal: {numero_decimal}, em octal é: {numero_octal[2:]}')


def hexadecimal_para_octal():
    
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
    soma = oct(soma)

    print(f'o número hexadecimal: {numero_hexadecimal_original}, em octal é: {soma[2:].upper()}')
