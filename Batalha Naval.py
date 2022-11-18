from random import randint
import random

campoJ=[[0]*10, 
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10]

campoPC=[[0]*10, 
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10]




def colocarEmbarc():
    for i in range(5):
        linha=int(input(f"Informe a linha da {i+1} embarcação (entre 0 e 4): "))
        if linha<=0 or linha>=4:
            print("Favor insira um valor válido")
            break
        else:
            coluna=int(input(f"Informe a coluna da {i+1} embarcação (entre 0 e 9): "))
            if coluna<0 or coluna>9:
                print("Favor insira um valor válido")
                break
            else:
                campoJ[linha][coluna]='X'
                print("Seu Tabuleiro:")
                for i in range(5):
                    print(campoJ[i])
                return campoJ

def test():
    for i in range(5):
        linha=random.randint(0, 4)
        coluna=random.randint(0, 9)
        campoJ[linha][coluna]='X'
    print("Seu Tabuleiro:")
    for i in range(5):
        print(campoJ[i])
    return campoJ

def embarPC():
    for i in range(5):
        linha=random.randint(0, 4)
        coluna=random.randint(0, 9)
        campoPC[linha][coluna]='X'
    return campoPC

def jogada():
    contJ=0
    contPC=0
    while contJ<=4:

        print("Hora de jogar!")
        linhaJogada=int(input("Escolha em qual linha deseja jogar: "))
        colunaJogada=int(input("Escolha em qual coluna deseja jogar: "))
        if campoPC[linhaJogada][colunaJogada]=='X':
            contJ=contJ+1
            print(f"FOGO!\nVocê acertou um navio inimigo\nO inimigo ainda tem {5-contJ} embarcações")
            print(f"Você ainda tem {5-contPC} embarcações")
            print('-='*30)
            campoPC[linhaJogada][colunaJogada]=0
            
            
        else:
            print("água")
            print(f"O inimigo ainda tem {5-contJ} embarcações")
            print('-='*30)
        
        linhaJogadaPC=random.randint(0, 4)
        colunaJogadaPC=random.randint(0, 9)
        if campoJ[linhaJogadaPC][colunaJogadaPC]=='X':
            contPC=+1
            print(f"FOGO!\nO inimigo acertou um navio aliado\nVocê ainda tem {5-contPC} embarcações")
            print(f"O inimigo ainda tem {5-contJ} embarcações")
            print('-='*30)
            campoJ[linhaJogadaPC][colunaJogadaPC]='O'
            print("Seu tabuleiro:")
            for i in range(5):
                print(campoJ[i])
        else:
            print("água")
            print('-='*30)
            print(f"Você ainda tem {5-contPC} embarcações")
            print("Seu tabuleiro:")
            for i in range(5):
                print(campoJ[i])
        
    if contJ>contPC:
        print("PARABENS voce venceu!!")
    else:
        print("Você perdeu")
#colocarEmbarc()
#test()
#embarPC()
#jogada()

def menu():
    print("Bem-vindo ao Menu do nosso jogo")
    escolha=int(input("Escolha dentre as opções a seguir: \n1 - Iniciar jogo\n2 - Link para o vídeo do grupo \n3 - Tutorial \n4 - Créditos e agradecimentos\nEscolha: "))
    if escolha==1:
        colocarEmbarc()
        embarPC()
        jogada()
    elif escolha==2:
        print("")
    elif escolha==3:
        print("\nAo iniciar o jogo, você terá a oportunidade de escolher a posição de suas 5 embarcações,\natravés das coordenadas (linhas e colunas), elas ficão marcadas como 'X', enquato a água será marcada como '0',\ne 'O' para tiros na água.\n  ")
        print('=-'*30)
        print("Inicio do Jogo\n\nVocê começará jogando, escolha uma linha e uma coluna para seu ataque,\nmas lembre-se, as linhas começam no 0 vão até 4, e as colunas até 9.\n")
        print("Após o primeiro ataque, será a vez do computador, e assim sucessivamente, até que você ou o computador, fique sem embarcações.\n")
    elif escolha==4:
        print('=-'*30)
        print("Integrantes:\n\nJoão Merlin \nPedro Henrique\n")
        print("Um agradecimento especial a Professora Marina, graças ao seu esforço e empenho para manter uma boa didatica,\ne suas madrugadas sacrificadas, para fornecer um execelente material de estudos que esse trabalho foi possível.")
        print("Sabemos que, infelizmente, esse esforço não é devidamente valorizado.\nMas gostaríamos que soubesse que você foi a melhor professora que tivemos esse semestre, e que, toda sua dedicação fez sim uma grande difereça para nós.")
        print("Espero que possamos te ter como professora no futuro\n")
    else:
        print("Vamos Usuário, você é melhor do que isso.")
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print('=-'*30)
        menu()
menu()