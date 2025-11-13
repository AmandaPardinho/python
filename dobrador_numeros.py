while(True):
    numero = input("Digite um número inteiro: ")
    try:
        numInt = int(numero)
        break
    except ValueError:
        print("O número digitado não é um número inteiro.")

dobro = numInt * 2

print(f"O dobro do número digitado é {dobro}")
