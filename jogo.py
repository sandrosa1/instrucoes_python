def partida():
    if(esc == "1"):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if(n % (m + 1) == 0):
            print()
            print("Voce começa!")
            UR = usuario_escolhe_jogada(n, m)
            n = n - UR 
            i = 1
        else:
            print()
            print("Computador começa!")
            a = computador_escolhe_jogada(n, m)
            n = n - a
            i = 2
        while(n != 0):
            if(i % 2 != 0):
                a = computador_escolhe_jogada(n, m)
                n = n - a
                i = i + 1
            else:
                UR = usuario_escolhe_jogada(n, m)
                n = n  - UR
                i = i + 1
            
        print("Fim do jogo! O computador ganhou!")
        print()
        print("**** Final da partida! ****")
        print()
        print("Placar: Você 0 X 1 Computador")
    else:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if(n % (m + 1) == 0):
            print()
            print("Voce começa!")
            UR = usuario_escolhe_jogada(n, m)
            n = n - UR 
            i = 1
        else:
            print()
            print("Computador começa!")
            a = computador_escolhe_jogada(n, m)
            n = n - a
            i = 2
        while(n != 0):
            if(i % 2 != 0):
                a = computador_escolhe_jogada(n, m)
                n = n - a
                i = i + 1
            else:
                UR = usuario_escolhe_jogada(n, m)
                n = n  - UR
                i = i + 1
            
        print("Fim do jogo! O computador ganhou!")
        print()
        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você 0 X 3 Computador")


def computador_escolhe_jogada(n, m):
    i=1
    while((n - i) % (m + 1) != 0 and i <= m):
        i = i + 1
    if(i == 1) and (n - i == 0):
        print()
        print("O computador tirou uma peça.")
        return i
    elif((i == 1) and (n - i != 0)):
        print()
        print("O computador tirou uma peça.")
        print("Agora restam",n - i,"peças no tabuleiro.")
        return i
    elif( i > 1 ) and ( n - i == 0):
        print()
        print("O computador tirou",i,"peças.")
        return i
    else:
        print()
        print("O computador tirou",i,"peças.")
        print("Agora restam",n - i,"peças no tabuleiro.")
        return i

def usuario_escolhe_jogada(n, m):
    print()
    UR = int(input("Quantas peças voce vai tirar? "))
    if(UR == 1):
        print()
        print("Voce tirou uma peça.")
        if((n - UR) == 1):
            print("Agora resta apenas uma peça no tabuleiro.") 
        else:
            print("Agora restam",n - UR,"peças no tabuleiro.")
        return UR
    elif(UR <= m):
        print()
        print("Voce tirou",UR,"peças.")
        if((n - UR) == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n - UR,"peças no tabuleiro.")
        return UR
    elif(UR <= 0 or UR > m):
        print()
        print("Oops! Jogada invalida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)






ini = 0
while (ini == 0):
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print ("1 - para jogar uma partida isolada")
    esc = (input("2 - para jogar um campeonato "))
    if(esc == "1"):
        ini = 1
        print()
        print("Voce escolheu uma partida isolada!")
        print()
        partida()
    elif(esc == "2"):
        print()
        print("Voce escolheu um campeonato!")
        cont = 1
        ini = 1
        while(cont <= 3):
            print()
            print("**** Rodada",cont,"****")
            print()
            cont = cont + 1
            partida()
   
    else:
        print()
        print("Valor invalido!")
        
        


