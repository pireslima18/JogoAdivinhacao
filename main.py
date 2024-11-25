import random
import sys
print("***********************")
print("Vamos começar os jogos")
print("***********************")

pontos = 1000
totalTentativas = 0
numero = random.randrange(1, 101)
print("Escolha a dificuldade do jogo:")
try:
    nivelJogo = int(input("[ 1 ] Fácil \n[ 2 ] Médio \n[ 3 ] Dificil \nSelecione a opção: "))
except ValueError:
    nivelJogo = 0
match nivelJogo:
    case 1:
        totalTentativas = 10
    case 2:
        totalTentativas = 6
    case 3:
        totalTentativas = 3
    case _:
        print("Opção inválida")


for rodada in range(1, totalTentativas + 1):
    print(f"Tentativas restantes: {totalTentativas + 1 - rodada}")
    entrada = int(input("Tente adivinhar o número: "))
    menor = entrada < numero
    maior = entrada > numero

    if (entrada < 0 or entrada > 100):
        print("Digite um número entre 0 e 100")
        continue
    if (entrada == numero):
        print("Acertou")
        print(f"Total de pontos: {pontos}")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

        dif_numeros = numero - entrada
        pontos -= pontos - abs(dif_numeros)
    print("***********************\n")
print(f"O numero secreto era {numero}\n")
print("Fim do Jogo!")