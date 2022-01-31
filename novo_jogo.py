print("*************************")
print("*****Seja bem vindo*****!")
print("*************************")

secret_number = 42
tries = 3

for turn in range (1, tries +1):
    print("Tentativa", turn, "de", tries)
    kick_str = input("Digite um número entre 1 e 100: ")
    kick = int(kick_str)

    if (kick <1 or kick >100):
        print("Digite um número entre 1 e 100")
        continue

    hit = kick == secret_number
    bigger = kick > secret_number
    smaller = kick < secret_number

    if (hit):
        print("Parabéns! Você acertou")
        break

    else:
        if (bigger):
            print("Você errou! O número que você escolheu é maior que o número secreto...")

        elif (smaller):
            print("Você errou! O número escolhido é menor que o número secreto...")

    turn = turn +1

print("FIM DO JOGO")

