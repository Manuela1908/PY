#chamar a função 'codificar'
def codificar():

    try:

        numero = int(input("Digite um número inteiro positivo: "))#pedir o número a ser convertido
        
        #o usuário é capaz de tudo
        if numero < 0:
            print("O número deve ser positivo.")
        elif numero == 0:
            print("O número em binário é: 0")
            
        #converter a base do número oferecido em binário, utilizando a divisão dos restos por 2, sucessivamente
        else:
            binario = ""
            while numero > 0:
                resto = numero % 2
                binario = str(resto) + binario
                numero = numero // 2
                
        print(f"o número em binário é: {binario}")
        
    #o usuário é capaz de tudo     
    except ValueError:
        print("Caractere inválido, digite um número positivo")


#chamar a função 'decodificar'
def decodificar():

    
    while True:
        numero_binario = input("Digite um número binário: ")
        if numero_binario.isdigit() and set(numero_binario) <= set('01'):
            decimal = int(numero_binario, 2)
            print(f"O número {numero_binario} representa o número ({decimal}) na base 10")
            break
        else:
            print("Número inválido. Digite apenas 0 e 1.")#o usuário é capaz de tudo



opcoes = {
    1: codificar,
    2: decodificar,
}

opcao = int(input("Digite 1 para codificar, ou 2 para decodificar: "))

if opcao in opcoes:
    opcoes[opcao]()
else:
    print("Opção inválida")#o usuário é capaz de tudo
    
