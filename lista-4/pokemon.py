# 0: nome | 1: tipo | 2: hp | 3: defesa | 4: nome ataque | 5: poder ataque | 6: tipo ataque | 7: velocidade

def calcularDano(nomeAtac, poderAtac, defesa, tipoAtac, tipoDef, vidaDef, vidaMaxDef, nomeDef): #* int
    dano = poderAtac - (defesa / 2)

    listaTipos = [tipoAtac, tipoDef]
    
    if listaTipos == ["fogo", "grama"] or listaTipos == ["agua", "fogo"] or listaTipos == ["grama", "agua"] or listaTipos == ["eletrico", "agua"]:
        dano *= 2
        print(f"{nomeAtac} é super efetivo!")
    elif listaTipos == ["grama", "fogo"] or listaTipos == ["fogo", "agua"] or listaTipos == ["agua", "grama"] or listaTipos == ["agua", "eletrico"]:
        dano *= 0.5
        print(f"{nomeAtac} não é muito efetivo...")
    
    if dano == 0: dano = 1
    vidaAtual = vidaDef - int(dano)
    if vidaAtual < 0: vidaAtual = 0

    print(f"Causou {int(dano)} de dano. HP de {nomeDef} agora é {vidaAtual}/{vidaMaxDef}.")
    return vidaAtual

def calcularOrdem(velJogador, velOponente): #* str
    primeiro = "jogador" if velJogador >= velOponente else "oponente"
    return primeiro

def main():
    timeLorelei = [["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
                   ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
                   ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
                   ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]]
    
    timeBruno = [["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
                 ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
                 ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
                 ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]]
    
    timeAgatha = [["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
                  ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
                  ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
                  ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]]
    
    timeLance = [["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
                 ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
                 ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
                 ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]]

    strPokemon = ""
    timeJogador = []
    oponenteEscolhido = ""
    timeOponente = []

    rodadaAtual = 1
    pontosOponente = 0
    pontosJogador = 0

    # 0: nome | 1: tipo | 2: hp | 3: defesa | 4: nome ataque | 5: poder ataque | 6: tipo ataque | 7: velocidade
    print("Hora de montar seu time Pokémon!")
    for i in range(4):
        strPokemon = input()
        timeJogador.append(strPokemon.split(" - "))
        for j in range(len(timeJogador[i])):
            if timeJogador[i][j].isnumeric(): timeJogador[i][j] = int(timeJogador[i][j])

    print()
    print("Qual membro da Elite Four você deseja enfrentar?")
    oponenteEscolhido = input()
    if oponenteEscolhido == "lorelei": timeOponente = timeLorelei
    elif oponenteEscolhido == "bruno": timeOponente = timeBruno
    elif oponenteEscolhido == "agatha": timeOponente = timeAgatha
    else: timeOponente = timeLance
    print()

    print("====================")
    print("A BATALHA VAI COMEÇAR!")
    print("====================")
    # rodadas
    vidaAtualJogador = timeJogador[0][2]
    vidaAtualOponente = timeOponente[0][2]
    while len(timeOponente) > 0 and len(timeJogador) > 0:
        pokeJogador = timeJogador[0]
        pokeOponente = timeOponente[0]

        turnoAtual = 1

        print()
        print(f"--- Rodada {rodadaAtual} ---")
        print(f"{pokeJogador[0]}, eu escolho você!")
        print(f"{pokeOponente[0]}, vai!")
        print("--------------------")
        # turnos
        primeiraPessoa = calcularOrdem(pokeJogador[7], pokeOponente[7])
        while vidaAtualJogador > 0 and vidaAtualOponente > 0:
            print()
            print(f"-- Turno {turnoAtual} --")
            print()

            if primeiraPessoa == "jogador":
                print(f"{pokeJogador[0]} usa {pokeJogador[4]}!")
                vidaAtualOponente = calcularDano(pokeJogador[4], pokeJogador[5], pokeOponente[3], pokeJogador[6], pokeOponente[1], vidaAtualOponente, pokeOponente[2], pokeOponente[0])
                if vidaAtualOponente > 0:
                    print()
                    print(f"{pokeOponente[0]} do oponente usa {pokeOponente[4]}!")
                    vidaAtualJogador = calcularDano(pokeOponente[4], pokeOponente[5], pokeJogador[3], pokeOponente[6], pokeJogador[1], vidaAtualJogador, pokeJogador[2], pokeJogador[0])
            else: # "oponente"
                print(f"{pokeOponente[0]} do oponente usa {pokeOponente[4]}!")
                vidaAtualJogador = calcularDano(pokeOponente[4], pokeOponente[5], pokeJogador[3], pokeOponente[6], pokeJogador[1], vidaAtualJogador, pokeJogador[2], pokeJogador[0])
                if vidaAtualJogador > 0:
                    print()
                    print(f"{pokeJogador[0]} usa {pokeJogador[4]}!")
                    vidaAtualOponente = calcularDano(pokeJogador[4], pokeJogador[5], pokeOponente[3], pokeJogador[6], pokeOponente[1], vidaAtualOponente, pokeOponente[2], pokeOponente[0])

            turnoAtual += 1

        print()

        if vidaAtualOponente == 0:
            print(f"{pokeOponente[0]} do oponente foi derrotado!")
            timeOponente.pop(0)
            if len(timeOponente) > 0: vidaAtualOponente = timeOponente[0][2]
            pontosJogador += 1
        else:
            print(f"{pokeJogador[0]} foi derrotado!")
            timeJogador.pop(0)
            if len(timeJogador) > 0: vidaAtualJogador = timeJogador[0][2]
            pontosOponente += 1

        print()
        print("--------------------")
        print()
        print(f"Placar: {pontosJogador} X {pontosOponente}")
        rodadaAtual += 1
    
    print()
    if len(timeOponente) == 0:
        print("========================================")
        print("Parabéns! Você venceu a batalha Pokémon!")
        print("========================================")
    else:
        print("========================================")
        print("Que pena! Você foi derrotado.")
        print("========================================")
    
main()