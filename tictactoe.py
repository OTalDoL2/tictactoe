import os 
import copy

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogadasPossiveis(board):
    jogadas = []
    for i in range(3):
        for j in range(3):
            # print(f'Se liga na posição {board[i][j]}')
            if board[i][j] == "":
                jogadas.append([i, j])
    return jogadas

def minimax(board, jogador, jogadorDaVez):
    endGame = jogadasFinais(board, jogadorDaVez)
    if endGame == jogadorDaVez: return 1
    if endGame != jogadorDaVez and endGame != "velha" : return -1
    if endGame == "velha": return 0

    jogadas = jogadasPossiveis(board)

    #Max
    if jogador == jogadorDaVez:
        melhorValor = float('-inf')
        for i in jogadas:
            if jogadorDaVez == 'x':
                proximoJogador = 'o' 
            
            else:
                proximoJogador = 'o'

            resultado = analisarJogada(board, jogadas[i], jogador)
            valor = minimax(resultado, proximoJogador, jogadorDaVez)
            if valor > melhorValor:
                melhorValor = valor
        return melhorValor
        
    else:
        melhorValor = float('-inf')
        for i in jogadas:
            if jogadorDaVez == 'x':
                proximoJogador = 'o' 
            
            else:
                proximoJogador = 'o'

            resultado = analisarJogada(board, jogadas[i], jogador)
            valor = minimax(resultado, proximoJogador, jogadorDaVez)
            if valor < melhorValor:
                melhorValor = valor
        return melhorValor


    #Min


def analisarJogada(board, posicaoX, posicaoY, jogadorDaVez):
    # novoBoard = copy.deepcopy(board)
    board[posicaoX, posicaoY] = jogadorDaVez
    return novoBoard

def melhorJogada(board, jogadorDaVez):
    jogadas = jogadasPossiveis(board)
    for i in jogadas:
        resultado = analisarJogada(board, int(i[0]), int(i[1]), jogadorDaVez)
        proximoJogador = ''
        
        if jogadorDaVez == 'x':
            proximoJogador = 'o' 
        
        else:
            proximoJogador = 'o'

        valor = minimax(resultado, proximoJogador, jogadorDaVez)
        melhorValor = float('-inf')
        if valor > melhorValor:
            melhorAlternativa = jogadas[i]
    return melhorAlternativa


def jogadasFinais(matriz, jogadorDaVez):
    # Linha um completa
    if(matriz[0][0] == jogadorDaVez and matriz[0][1] == jogadorDaVez and matriz[0][2] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    # Linha dois completa
    elif(matriz[1][0] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[1][2] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    # Linha tr^es completa
    elif(matriz[2][0] == jogadorDaVez and matriz[2][1] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    # Coluna um completa
    elif(matriz[0][0] == jogadorDaVez and matriz[1][0] == jogadorDaVez and matriz[2][0] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez
        
    # Coluna dois completa
    elif(matriz[0][1] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][1] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    # Coluna tres completa
    elif(matriz[0][2] == jogadorDaVez and matriz[1][2] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    #cruzados
    elif(matriz[0][0] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez

    elif(matriz[0][2] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][0] == jogadorDaVez):
        print(f"Parabens, o jogador {jogadorDaVez} ganhou!")
        return jogadorDaVez
    
    # Vai verificar se todos os campos estão preenchidos, "Deu Velha"
    elif all(all(i != "" for i in row) for row in matriz):
        print("Deu velha, tente novamente!")
        return "velha"

    else:
        return 0

def versusBot():
    posicaoTabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

    linha1 = "1  ___|___|___"
    linha2 = "2  ___|___|___"
    linha3 = "3     |   |   "

    cond = 0

    rodada = 0

    jogadorDaVez = ""
    while cond == 0:
        
        print(f"\n    1   2   3\n{linha1}\n{linha2}\n{linha3}\n")

        if rodada % 2 == 0:
            jogadorDaVez = "x"
            linha = int(input("Digite o num da sua linha ")) 
            coluna = int(input("Digite o num da sua coluna "))

            if posicaoTabuleiro[linha - 1][coluna - 1] == "x" or posicaoTabuleiro[linha - 1][coluna - 1] == "o":
                print("esse espaço foi preencido, tente novamente!")
            else:
                posicaoTabuleiro[linha - 1][coluna - 1] = jogadorDaVez

                if linha == 1:
                    if coluna == 1:
                        linha1 = linha1[:4] + jogadorDaVez + linha1[5:]
                    elif coluna == 2:
                        linha1 = linha1[:8] + jogadorDaVez + linha1[9:]
                    elif coluna == 3:
                        linha1 = linha1[:12] + jogadorDaVez + linha1[13:]


                elif linha == 2:
                    if coluna == 1:
                        linha2 = linha2[:4] + jogadorDaVez + linha2[5:]
                    elif coluna == 2:
                        linha2 = linha2[:8] + jogadorDaVez + linha2[9:]
                    elif coluna == 3:
                        linha2 = linha2[:12] + jogadorDaVez + linha2[13:]


                elif linha == 3:
                    if coluna == 1:
                        linha3 = linha3[:4] + jogadorDaVez + linha3[5:]
                    elif coluna == 2:
                        linha3 = linha3[:8] + jogadorDaVez + linha3[9:]
                    elif coluna == 3:
                        linha3 = linha3[:12] + jogadorDaVez + linha3[13:]
                
                
     
                if rodada >= 3: 
                    cond = jogadasFinais(posicaoTabuleiro, jogadorDaVez)
                
                if cond == 1:

                    restart = input("\nDeseja continuar jogando?")
                    
                    if restart == "1" or restart == "sim" or "Sim" or "s":
                        cond = 0
                        posicaoTabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

                        linha1 = "1  ___|___|___"
                        linha2 = "2  ___|___|___"
                        linha3 = "3     |   |   "
        else: 
            jogadorDaVez = "o"
            melhorJogada(posicaoTabuleiro, jogadorDaVez)


       
                    
        rodada += 1


def versusPlayer():
    posicaoTabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

    linha1 = "1  ___|___|___"
    linha2 = "2  ___|___|___"
    linha3 = "3     |   |   "

    cond = 0

    rodada = 0

    jogadorDaVez = ""
    while cond == 0:
        if rodada % 2 == 0:
            jogadorDaVez = "x"
        else: 
            jogadorDaVez = "o"

        print(f"\n    1   2   3\n{linha1}\n{linha2}\n{linha3}\n")

        linha = int(input("Digite o num da sua linha ")) 
        coluna = int(input("Digite o num da sua coluna "))

        if posicaoTabuleiro[linha - 1][coluna - 1] == "x" or posicaoTabuleiro[linha - 1][coluna - 1] == "o":
            print("esse espaço foi preencido, tente novamente!")
        else:
            posicaoTabuleiro[linha - 1][coluna - 1] = jogadorDaVez

            if linha == 1:
                if coluna == 1:
                    linha1 = linha1[:4] + jogadorDaVez + linha1[5:]
                elif coluna == 2:
                    linha1 = linha1[:8] + jogadorDaVez + linha1[9:]
                elif coluna == 3:
                    linha1 = linha1[:12] + jogadorDaVez + linha1[13:]


            elif linha == 2:
                if coluna == 1:
                    linha2 = linha2[:4] + jogadorDaVez + linha2[5:]
                elif coluna == 2:
                    linha2 = linha2[:8] + jogadorDaVez + linha2[9:]
                elif coluna == 3:
                    linha2 = linha2[:12] + jogadorDaVez + linha2[13:]


            elif linha == 3:
                if coluna == 1:
                    linha3 = linha3[:4] + jogadorDaVez + linha3[5:]
                elif coluna == 2:
                    linha3 = linha3[:8] + jogadorDaVez + linha3[9:]
                elif coluna == 3:
                    linha3 = linha3[:12] + jogadorDaVez + linha3[13:]
            
            if rodada >= 3: 
                cond = jogadasFinais(posicaoTabuleiro, jogadorDaVez)
            
            if cond == 1:

                restart = input("\nDeseja continuar jogando?")
                
                if restart == "1" or restart == "sim" or "Sim" or "s":
                    cond = 0
                    posicaoTabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

                    linha1 = "1  ___|___|___"
                    linha2 = "2  ___|___|___"
                    linha3 = "3     |   |   "
                    

            rodada += 1



# time.sleep(0.6)
# print("                                #")
# time.sleep(0.6)
# print("                                #  ####   ####   ####        #####    ##         #     # ###### #      #    #   ##   ")
# time.sleep(0.6)
# print("                                # #    # #    # #    #       #    #  #  #        #     # #      #      #    #  #  #  ")
# time.sleep(0.6)
# print("                                # #    # #      #    #       #    # #    #       #     # #####  #      ###### #    # ")
# time.sleep(0.6)
# print("                          #     # #    # #  ### #    #       #    # ######        #   #  #      #      #    # ###### ")
# time.sleep(0.6)
# print("                          #     # #    # #    # #    #       #    # #    #         # #   #      #      #    # #    # ")
# time.sleep(0.6)
# print("                           #####   ####   ####   ####        #####  #    #          #    ###### ###### #    # #    # ")
# time.sleep(3)

player = int(input("\n\nDigite 1 para jogar uma partida contra a maquina\nDigite 2 para jogar uma partida 1x1\n"))
if player == 1:
    versusBot()
else:
    versusPlayer()



    

