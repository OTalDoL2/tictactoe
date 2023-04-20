import os 

linha1 = "1  ___|___|___"
linha2 = "2  ___|___|___"
linha3 = "3     |   |   "


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogadasFinais(matriz, peca, valorRetorno):
    # Linha um completa
    valorRetorno = valorRetorno % 2 
          
    

    if(matriz[0][0] == jogadorDaVez and matriz[0][1] == jogadorDaVez and matriz[0][2] == jogadorDaVez):
        return 1

    # Linha dois completa
    elif(matriz[1][0] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[1][2] == jogadorDaVez):
        return 1

    # Linha tr^es completa
    elif(matriz[2][0] == jogadorDaVez and matriz[2][1] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        return 1

    # Coluna um completa
    elif(matriz[0][0] == jogadorDaVez and matriz[1][0] == jogadorDaVez and matriz[2][0] == jogadorDaVez):
        return 1
        
    # Coluna dois completa
    elif(matriz[0][1] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][1] == jogadorDaVez):
        return 1

    # Coluna tres completa
    elif(matriz[0][2] == jogadorDaVez and matriz[1][2] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        return 1


    #cruzados
    elif(matriz[0][0] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][2] == jogadorDaVez):
        return 1

    elif(matriz[0][2] == jogadorDaVez and matriz[1][1] == jogadorDaVez and matriz[2][0] == jogadorDaVez):
        return 1

    else:
        return 0

pos = [["", "", ""], ["", "", ""], ["", "", ""]]

cond = 0

rodada = 0

jogadorDaVez = ""
while cond == 0:
    if rodada % 2 == 0:
        jogadorDaVez = "x"
    else: 
        jogadorDaVez = "o"

    print(f"    1   2   3\n{linha1}\n{linha2}\n{linha3}")
    linha = int(input("Digite o num da sua linha ")) 
    coluna = int(input("Digite o num da sua coluna "))

    if pos[linha - 1][coluna - 1] == "x" or pos[linha - 1][coluna - 1] == "o":
        print("esse espaço foi preencido, tente novamente!")
    else:
        pos[linha - 1][coluna - 1] = jogadorDaVez

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
                linha3 = linha3[:4] + jogadorDaVez + linha2[5:]
            elif coluna == 2:
                linha3 = linha3[:8] + jogadorDaVez + linha3[9:]
            elif coluna == 3:
                linha3 = linha3[:12] + jogadorDaVez + linha3[13:]
        if rodada >= 3: 
            cond = jogadasFinais(pos, jogadorDaVez, rodada)

        rodada += 1
    


if cond == 1:
    print("Parabens, o X ganhou!")
else:
    print("Parabens, o O ganhou!")
print("FIM")