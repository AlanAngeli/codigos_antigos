import forca
import adivinhacao_pontos


print("****************************")
print("Escolha seu jogo!")
print("****************************")

print("(1)Forca (2)Adivinhação")

game = int(input("Qual jogo? "))

if(game == 1):
    print("Jogo da forca")
    forca.play()
elif(game == 2):
    print("Jogo da adivinhação")
    adivinhacao_pontos.play()

