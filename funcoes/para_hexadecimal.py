def binario_para_hexadecimal():
   
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
    resultado_final = hex(soma)

    print(f'o número binário: {numero_binario}, em decimal é: {resultado_final[2:].upper()}')


def octal_para_hexadecimal():
    
    numero_octal_original = input('Digite um número octal: ')
    numero_octal = list(numero_octal_original)

    # VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['8', '9']
    for numero in numeros_invalidos:
        if numero in str(numero_octal):
            print('Número inválido')
            return
    
    #VARIÁVEIS
    tamanho_potencia = len(numero_octal)
    i = 0
    j = tamanho_potencia - 1
    soma = 0

    #CONVERSÃO DO NÚMERO
    for numero in numero_octal:
        resultado = int(numero) * (8**j)
        soma += resultado
        i += 1
        j -= 1
    soma = hex(soma)
    print(f'o número octal: {numero_octal_original}, em decimal é: {soma[2:].upper()}')


def decimal_para_hexadecimal():
    
    numero_decimal = int(input('Digite um número decimal: '))
    numero_hexadecimal = hex(numero_decimal)

    print(f'o número decimal: {numero_decimal}, em hexadecimal é: {numero_hexadecimal[2:].upper()}')
