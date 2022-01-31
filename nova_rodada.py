print("*************************")
print("BEM VINDO")
print("*************************")

secret_number = 42
turn = 1
tries = 3

while(turn <= tries):
    print("Rodada", turn, "de", tries,)
    kick_str = input("Digite seu chute: ")
    kick = int(kick_str)

    hit = kick == secret_number
    bigger = kick > secret_number
    smaller = kick < secret_number

    if (hit):
        print("Você acertou!!! O número escolhido é", secret_number, "!!!")
    else:

        if(bigger):
            print("Você errou! Seu chute foi maior que o número secreto.")

        elif(smaller):
            print("Você errou! Seu chute foi menor que o número escolhido.")
    turn = turn +1

print("FIM DO JOGO")


