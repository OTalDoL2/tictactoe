import numpy as np


linha1 = "1  ___|___|___"
linha2 = "2  ___|___|___"
linha3 = "3     |   |   "




pos = [["", "", ""], ["", "", ""], ["", "", ""]]

cond = 0
while cond == 0:
    print(f"    1   2   3\n{linha1}\n{linha2}\n{linha3}")
    linha = int(input("Digite o num da sua linha ")) 
    coluna = int(input("Digite o num da sua coluna "))

    pos[linha - 1][coluna - 1] = "x"

    if linha == 1:
        if coluna == 1:
            linha1 = linha1[:4] + "x" + linha1[5:]
        elif coluna == 2:
            linha1 = linha1[:8] + "x" + linha1[9:]
        elif coluna == 3:
            linha1 = linha1[:12] + "x" + linha1[13:]


    elif linha == 2:
        if coluna == 1:
            linha2 = linha2[:4] + "x" + linha2[5:]
        elif coluna == 2:
            linha2 = linha2[:8] + "x" + linha2[9:]
        elif coluna == 3:
            linha2 = linha2[:12] + "x" + linha2[13:]


    elif linha == 3:
        if coluna == 1:
            linha3 = linha3[:4] + "x" + linha2[5:]
        elif coluna == 2:
            linha3 = linha3[:8] + "x" + linha3[9:]
        elif coluna == 3:
            linha3 = linha3[:12] + "x" + linha3[13:]
            
    if(pos[0][0] == "x" and pos[0][1] == "x" and pos[0][2] == "x"):
        linha1 = linha1.replace("_", "-")
        cond = 1
    elif(pos[1][0] == "x" and pos[1][1] == "x" and pos[1][2] == "x"):
        linha2 = linha2.replace("_", "-")
        cond = 1
    elif(pos[2][0] == "x" and pos[2][1] == "x" and pos[2][2] == "x"):
        linha3 = linha3.replace("_", "-")
        cond = 1

    elif(pos[0][0] == "x" and pos[1][0] == "x" and pos[2][0] == "x"):
        cond = 1
        linha1 = linha1.replace("x", "|")
        linha2 = linha2.replace("x", "|")
        linha3 = linha3.replace("x", "|")
        
    elif(pos[0][1] == "x" and pos[1][1] == "x" and pos[2][1] == "x"):
        linha1 = linha1.replace("x", "|")
        linha2 = linha2.replace("x", "|")
        linha3 = linha3.replace("x", "|")
        cond = 1

    elif(pos[0][2] == "x" and pos[1][2] == "x" and pos[2][2] == "x"):
        linha1 = linha1.replace("x", "|")
        linha2 = linha2.replace("x", "|")
        linha3 = linha3.replace("x", "|")
        cond = 1
    
    elif(pos[0][2] == "x" and pos[1][1] == "x" and pos[2][0] == "x"):
        cond = 1

    elif(pos[0][0] == "x" and pos[1][1] == "x" and pos[2][2] == "x"):
        cond = 1

print(f"    1   2   3\n{linha1}\n{linha2}\n{linha3}")
print("FIM")