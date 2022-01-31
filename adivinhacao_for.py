import random

print("****************************")
print("Bem vindo ao jogo de adivinhação!")
print("****************************")

secret_number = random.randrange(1, 101)
tries = 0

print("Escolha um nível de dificuldade")
print("(1) Fácil (2) Médio (3) Difícil")

level = int(input("Defina um nível: "))

easy = level == 1
normal = level == 2
hard = level == 3

if (easy):
    tries = 20
if (normal):
    tries = 10
elif (hard):
    tries = 5
elif (level <1 or level >3):
    print("Escolha um número entre 1 e 3")

print(secret_number)


for turn in range (1, tries +1):
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
