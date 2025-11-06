def distanciaChebyshev(xSam, ySam): #* int
    distancia = 0
    for i in range(6):
        for j in range(6):
            distancia = max(distancia, (abs(i - xSam)), (abs(j - ySam)))
    
    return distancia

def teleportarNeil(matriz, xSam, ySam, neilEmCimaP): #* list, int, int, boolean
    # troca o N com o piso onde ele estava em cima
    for i in range(len(matriz)):
        if "N" in matriz[i]:
            if neilEmCimaP:
                matriz[i][matriz[i].index("N")] = "P"    
            else:
                matriz[i][matriz[i].index("N")] = "F"

    ultimoI = 0
    ultimoJ = 0
    distCheby = distanciaChebyshev(xSam, ySam)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            # se a matriz estiver na linha ou coluna onde a distância
            # entre Sam e Neil após o teleporte for igual à de Chebyshev
            if (abs(i - xSam) == distCheby) or (abs(j - ySam) == distCheby):
                # pula os pisos I
                if matriz[i][j] != "I":
                    ultimoI = i
                    ultimoJ = j

    neilEmCimaP = False if matriz[ultimoI][ultimoJ] == "F" else True
    matriz[ultimoI][ultimoJ] = "N"

    return matriz, ultimoI, ultimoJ, neilEmCimaP

def tiroSam(arma, xSam, ySam, xNeil, yNeil): #* int
    dano = 0
    distanciaAtual = max(abs(xNeil - xSam), abs(yNeil - ySam))

    if arma == "Espingarda":
        if distanciaAtual <= 2:
            dano = 25
    elif arma == "Rifle":
        dano = 15 if distanciaAtual == 3 else 5
    else: # "Metralhadora"
        if distanciaAtual >= 4:
            dano = 15

    return dano

def validarMovimento(matriz, xDestino, yDestino): #* boolean
    # verifica se o destino não ultrapassa a matriz
    if (xDestino >= 0 and xDestino < 6) and (yDestino >= 0 and yDestino < 6):
        # verifica se o destino não é do piso I
        return True if (matriz[xDestino][yDestino] != "I") else False
    else: return False

def avisarPoucaVida(vidaSam, avisou): #* boolean
    if vidaSam <= 40 and not avisou:
        print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
        return True
    
def verificarOsDoisVivos(vidaSam, vidaNeil): #* boolean
    return True if vidaSam > 0 and vidaNeil > 0 else False

def main():
    print("Sam: Mas que lugar é esse aqui?")
    print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
    print()

    matriz = []
    vidaSam = vidaNeil = 100
    xSam = ySam = -1
    xNeil = yNeil = -1
    avisouPoucaVida = False

    movimentoValido = True
    samEmCimaP = True
    neilEmCimaP = True
    armaSam = "Rifle"
    tirosEmNeil = 0

    danoDeNeil = 0
    qtdQueimada = 0

    # preenchimento da matriz
    for i in range(6):
        linha = input()
        matriz.append(linha.split(" "))
        if "S" in matriz[i]:
            xSam = i
            ySam = matriz[i].index("S")
        if "N" in matriz[i]:
            xNeil = i
            yNeil = matriz[i].index("N")
    
    # combate
    while verificarOsDoisVivos(vidaSam, vidaNeil):
        # ações do Sam
        for i in range(4):
            if verificarOsDoisVivos(vidaSam, vidaNeil):
                acao = input()

                # AÇÃO - andar
                if acao in "WASD":
                    matriz[xSam][ySam] = "P" if samEmCimaP else "F"

                    if acao == "W":
                        movimentoValido = validarMovimento(matriz, xSam - 1, ySam)
                        if movimentoValido:
                            xSam -= 1
                    elif acao == "A":
                        movimentoValido = validarMovimento(matriz, xSam, ySam - 1)
                        if movimentoValido:
                            ySam -= 1
                    elif acao == "S":
                        movimentoValido = validarMovimento(matriz, xSam + 1, ySam)
                        if movimentoValido:
                            xSam += 1
                    else: # "D"
                        movimentoValido = validarMovimento(matriz, xSam, ySam + 1)
                        if movimentoValido:
                            ySam += 1

                    # verifica se ele vai pisar ou está pisando no F (movimento inválido e não sai do lugar)
                    if matriz[xSam][ySam] == "F" or (not samEmCimaP and not movimentoValido):
                        samEmCimaP = False
                        vidaSam -= 5
                        qtdQueimada += 1
                        if not avisouPoucaVida:
                            avisouPoucaVida = avisarPoucaVida(vidaSam, avisouPoucaVida)
                    else: samEmCimaP = True

                    matriz[xSam][ySam] = "S"
                else: # ele não andou, então tem que verificar se ele ficou parado no piso F
                    if not samEmCimaP: # está em cima do F
                        vidaSam -= 5
                        qtdQueimada += 1
                        if not avisouPoucaVida:
                            avisouPoucaVida = avisarPoucaVida(vidaSam, avisouPoucaVida)

                    # AÇÃO - atirar
                    if acao == "Atirar":
                        dano = tiroSam(armaSam, xSam, ySam, xNeil, yNeil)
                        if dano > 0:
                            vidaNeil -= dano
                            tirosEmNeil += 1
                        if tirosEmNeil == 3 and vidaNeil > 0: # verifica se o Neil vai teleportar
                            matriz, xNeil, yNeil, neilEmCimaP = teleportarNeil(matriz, xSam, ySam, neilEmCimaP)
                            tirosEmNeil = 0
                            for i in range(len(matriz)):
                                print(" ".join(matriz[i]))

                    # AÇÃO - troca de arma
                    else:
                        print(f"Arma trocada para {acao}.")
                        armaSam = acao
        
        # Neil atira
        if verificarOsDoisVivos(vidaSam, vidaNeil):
            print(">>> Você recebe um disparo de Neil! <<<")
            vidaSam -= 15
            danoDeNeil += 15
            if not avisouPoucaVida:
                avisouPoucaVida = avisarPoucaVida(vidaSam, avisouPoucaVida)

    print()
    if vidaNeil <= 0:
        likes = 1000 - (danoDeNeil * 8) - (qtdQueimada * 10)
        print("MISSÃO COMPLETA! - Investigue a Anomalia")
        print("========================================")
        print(f"Likes recebidos: 👍 {likes}")
    else:
        print("MISSÃO FALHOU")
        print("==============")
        print("Sam foi derrotado.")
        print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")

main()