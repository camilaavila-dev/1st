#Você conhece o jogo do NIM? 
#Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. 
#Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. 
#Quem tirar as últimas peças possíveis ganha o jogo.


def computador_escolhe_jogada(n,m):
    pc_remove = 1
    estrategia_pc = int(n % (m + 1))
    if n == m or estrategia_pc > m:
        pc_joga = int(m)
    else:
        pc_joga = estrategia_pc
    return pc_joga

def usuario_escolhe_jogada(n,m):
    user_joga = int(input("Quantas peças você você vai tirar?"))
    print(user_joga)
    print()
    if user_joga > m or user_joga < 1:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        user_joga = int(input("Quantas peças você mais retirar?","PS: máximo de peças é",m,"."))
    return user_joga

def partida():
    n = int(input("Quantas peças terá o tabuleiro? ")) 
    m = int(input("Qual vai ser o limite de peças por jogada? "))

    vez_do_pc = False

    if n % (m + 1) == 0:
        print("Você começa!") 
        print()
        usuario_escolhe_jogada
    
    else:
        print("Computador começa!")
        print()
        vez_do_pc = True
        computador_escolhe_jogada(n,m)
    
    next

    while n > 0:
        if vez_do_pc:
            pc_remove = computador_escolhe_jogada(n, m)
            n = n - pc_remove
            if pc_remove == 1:
                print("O computador tirou uma peça.")
                print()
            else:
                print("O computador tirou",pc_remove,"peças.")
                print()

            vez_do_pc = False
        else:
            user_remove = usuario_escolhe_jogada(n, m)
            n = n - user_remove
            if user_remove == 1:
                print("Você tirou uma peça.")
                print()
            else:
                print("Você tirou",user_remove,"peças.")
                print()
            vez_do_pc = True
        if n == 1:
            print("Resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam",n,"peças no tabuleiro.")
                print()
    print("Fim do jogo! O computador ganhou!")

    return computador_escolhe_jogada()
    return usuario_escolhe_jogada()

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print("**** Rodada,",numeroRodada,"****")
        print()
        partida()
        numeroRodada +=1
        print("Placar: Você 0 x 3 Computador")
        print()

#Inicio do jogo

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada.")
print("2 - para jogar um campeonato.")
print()
tipodepartida = int(input())
if tipodepartida == 1:
    print()
    print("Você escolheu uma partida isolada!")
    print()
    partida()
if tipodepartida == 2:
    print()
    print("Você escolheu um campeonato!")
    print()
    campeonato()
else:
    print("Opção inválida, escolha entre 1 e 2.")
    print()
