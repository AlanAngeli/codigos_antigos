print("*****************")
print("Seja bem vindo ao novo joga da adivinhação!")
print("*****************")

secret_number = 35
kick_str = input("Chute um número: ")

kick = int(kick_str)

hit = kick == secret_number
bigger = kick > secret_number
smaller = kick < secret_number

if (hit):
    print("Parabéns! Você acertou! O número secreto é", kick,"!")
else:
    if (bigger):
        print("Você errou :( ", "o número escolhido foi maior que o número secreto.")
    elif (smaller):
        print("Você errou :/", "O número escolhido foi menor que o número secreto.")

print("Fim do jogo")
