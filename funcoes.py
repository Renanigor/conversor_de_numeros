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

def binario_para_decimal():
   
    numero_binario = input('Digite um número binário: ')

    #VARIÁVEIS
    tamanho_potencia = len(numero_binario)
    i = 0
    j = tamanho_potencia - 1
    soma = 0
    
    #VALIDAÇÃO DO NÚMERO
    numeros_invalidos = ['2', '3', '4', '5,' '6', '7', '8,' '9']
    for numero in numeros_invalidos:
        if numero in str(numero_binario):
            print('Número inválido')
            return
        
    #CONVERSÃO DO NÚMERO
    for bit in numero_binario:
        resultado = int(bit) * int(numero_binario[i])
        multiplicacao = 2**j * resultado
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