bolasAndre = int(input())
bolasBruno = int(input())
bolasClara = int(input())

jogadaAndre = ""
jogadaBruno = ""
jogadaClara = ""

errosAndre = 0
errosBruno = 0
errosClara = 0

saiuAndre = False
saiuBruno = False
saiuClara = False

while not ((saiuAndre and saiuBruno) or (saiuAndre and saiuClara) or (saiuBruno and saiuClara)):
    # vez de ANDRÉ
    if (not saiuAndre and not saiuBruno) or (not saiuAndre and not saiuClara):
        jogadaAndre = input()
        if jogadaAndre == "acertou":
            bolasAndre += 2 if saiuBruno == False and saiuClara == False else 1
            bolasBruno -= 1
            bolasClara -= 1
            errosAndre = 0
        else: errosAndre += 1

        # VERFICAÇÃO DE ELIMINAÇÃO 1
        # verificação se André saiu
        if not saiuAndre:
            if bolasAndre <= 0:
                print("andre saiu do jogo")
                saiuAndre = True
            elif errosAndre >= 3:
                print("andre perdeu feio")
                saiuAndre = True
        # verificação se Bruno saiu
        if not saiuBruno:
            if bolasBruno <= 0:
                print("bruno saiu do jogo")
                saiuBruno = True
            elif errosBruno >= 3:
                print("bruno perdeu feio")
                saiuBruno = True
        # verificação se Clara saiu
        if not saiuClara:
            if bolasClara <= 0:
                print("clara saiu do jogo")
                saiuClara = True
            elif errosClara >= 3:
                print("clara perdeu feio")
                saiuClara = True

    # vez de BRUNO
    if (not saiuBruno and not saiuAndre) or (not saiuBruno and not saiuClara):
        jogadaBruno = input()
        if jogadaBruno == "acertou":
            bolasAndre -= 1
            bolasBruno += 2 if saiuAndre == False and saiuClara == False else 1
            bolasClara -= 1
            errosBruno = 0
        else: errosBruno += 1

        # VERFICAÇÃO DE ELIMINAÇÃO 2
        # verificação se André saiu
        if not saiuAndre:
            if bolasAndre <= 0:
                print("andre saiu do jogo")
                saiuAndre = True
            elif errosAndre >= 3:
                print("andre perdeu feio")
                saiuAndre = True
        # verificação se Bruno saiu
        if not saiuBruno:
            if bolasBruno <= 0:
                print("bruno saiu do jogo")
                saiuBruno = True
            elif errosBruno >= 3:
                print("bruno perdeu feio")
                saiuBruno = True
        # verificação se Clara saiu
        if not saiuClara:
            if bolasClara <= 0:
                print("clara saiu do jogo")
                saiuClara = True
            elif errosClara >= 3:
                print("clara perdeu feio")
                saiuClara = True

    # vez de CLARA
    if (not saiuClara and not saiuAndre) or (not saiuClara and not saiuBruno):
        jogadaClara = input()
        if jogadaClara == "acertou":
            bolasAndre -= 1
            bolasBruno -= 1
            bolasClara += 2 if saiuAndre == False and saiuBruno == False else 1
            errosClara = 0
        else: errosClara += 1

        # VERFICAÇÃO DE ELIMINAÇÃO 3
        # verificação se André saiu
        if not saiuAndre:
            if bolasAndre <= 0:
                print("andre saiu do jogo")
                saiuAndre = True
            elif errosAndre >= 3:
                print("andre perdeu feio")
                saiuAndre = True
        # verificação se Bruno saiu
        if not saiuBruno:
            if bolasBruno <= 0:
                print("bruno saiu do jogo")
                saiuBruno = True
            elif errosBruno >= 3:
                print("bruno perdeu feio")
                saiuBruno = True
        # verificação se Clara saiu
        if not saiuClara:
            if bolasClara <= 0:
                print("clara saiu do jogo")
                saiuClara = True
            elif errosClara >= 3:
                print("clara perdeu feio")
                saiuClara = True

vencedor = ""
if saiuAndre:
    if saiuBruno:
        vencedor = "clara"
    elif saiuClara:
        vencedor = "bruno"
else:
    vencedor = "andre"

print(f"{vencedor} ganhou")
print("a quantidade final de bolas foi:")
print(f"andre: {bolasAndre if bolasAndre > 0 else 0}\nbruno: {bolasBruno if bolasBruno > 0 else 0}\nclara: {bolasClara if bolasClara > 0 else 0}")