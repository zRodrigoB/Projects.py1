import Forca
import Advinhacao
def Jogos():
    print("**********************************")
    print("Escolha um jogo!!")
    print("**********************************")

    print("Digite (1) para o jogo da ADIVINHAÇÃO, ou digite (2) para o jogo da FORCA")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        Advinhacao.Jogar()
    elif(jogo == 2):
        Forca.Jogar()

if(__name__=="__main__"):
    Jogos()
