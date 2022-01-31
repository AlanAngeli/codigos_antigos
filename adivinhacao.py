print("****************************")
print("Bem vindo ao jogo de adivinhação!")
print("****************************")

secret_number = 42
tries = 3
turn = 1


while(turn <= tries):
    print("Tentativa", turn, "de", tries )
    kick_str = input("Digite o seu número:  ")
    print("Você digitou", kick_str)
    kick = int(kick_str)

    if (kick < 1 or kick > 100):
        print("Digite um número entre 1 e 100")
        continue

    hit = kick == secret_number
    bigger = kick > secret_number
    smaller = kick < secret_number

    if (hit):
        print("Você acertou! O número é", secret_number, "!!!")
        break
    else:
        if (bigger):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif (smaller):
            print("Você errou! Seu chute foi menor que o número secreto.")

    turn = turn +1

    print("Fim do jogo")
