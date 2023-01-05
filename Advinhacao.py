import random

def Jogar():

    print("**********************************")
    print("Bem vindo ao jogo de advinhação!!")
    print("**********************************")

    num_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    print (num_secreto)

    print(">>Escolha o nível de dificuldade<< \nDigite (1) para FÁCIL, (2) para NORMAL ou (3) para DIFÍCIL ")
    nivel = int (input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100: ")
            continue

        chute_foi_certo = num_secreto == chute
        chute_foi_maior = num_secreto < chute
        chute_foi_menor = num_secreto > chute

        if(chute_foi_certo):
            print("Parabéns!!! Você acertou e fez {} pontos!! ".format(pontos))
            break
        else:
            if(chute_foi_maior):
                print("Você errou!! seu chute foi maior que o número secreto")
            elif (chute_foi_menor):
                print("Você errou!! seu chute foi menor que o número secreto")
                pontos_perdidos = abs(num_secreto - chute)
                pontos = pontos - pontos_perdidos



    print("Fim de jogo")

if(__name__=="__main__"):
    Jogar()