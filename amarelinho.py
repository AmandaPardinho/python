
while(True):
    velocidade = input("Digite sua velocidade atual: ")
    
    try:
        velocidade_numero = int(velocidade)
        
        if(velocidade_numero > 80):
            maior_quanto = velocidade_numero - 80
            valor_multa = 7 * maior_quanto
            print(f"Velocidade acima da permitida. Você receberá uma multa no valor de R$ {valor_multa}")
            break
        else:
            print("Sua velocidade está dentro do limite permitido.")
            break
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")