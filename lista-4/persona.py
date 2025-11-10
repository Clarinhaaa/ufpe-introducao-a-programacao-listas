# FUNÇÕES diversas

def converterLista(lista):
    for i in range(len(lista)):
        if lista[i].isnumeric(): lista[i] = int(lista[i])
    return lista

def bubbleSort(lista): #* retorna as duas quantidades de trocas cres e decres
    listaCopia = lista.copy()
    qtdTrocasCres = 0
    qtdTrocasDecres = 0
    aux = 0

    # crescente
    for i in range(len(listaCopia) - 1):
        for j in range(len(listaCopia) - i - 1):
            if listaCopia[j] > listaCopia[j+1]:
                aux = listaCopia[j]
                listaCopia[j] = listaCopia[j+1]
                listaCopia[j+1] = aux
                qtdTrocasCres += 1

    # decrescente
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] < lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                qtdTrocasDecres += 1

    return qtdTrocasCres, qtdTrocasDecres

# FUNÇÕES relacionadas às sombras

def proximaSombraAlvo(sombras):
    # encontrando a sombra que Makoto irá atacar. Não deve estar derrubada
    somb = []
    idxSombraAlvo = -1

    encontrouOponente = False
    for s in sombras:
        if not s[4] and not encontrouOponente:
            somb = s
            idxSombraAlvo = sombras.index(s)
            encontrouOponente = True

    return somb, idxSombraAlvo

def derrotarSombra(sombraAlvo, idxSombra, sombras):
    if sombraAlvo[1] <= 0: print(f"Mitsuru: {sombras.pop(idxSombra)[0]} foi derrotado!")
    return sombras

# FUNÇÕES relacionadas aos turnos

def gerarRelatorioTurno(numTurno, makotoHp, sombras):
    print(f"TURNO {numTurno}:")
    print(f"HP Makoto: {makotoHp} / 300")
    
    for somb in sombras:
        print(f"HP {somb[0]}: {somb[1]} pontos de vida restantes")

    numTurno += 1

    return numTurno

def calcularPoderBase(golpe):
    atkMagicoLeve = ["Zio", "Garu", "Agi", "Bufu"]              # poder base: 3
    atkFisicoLeve = ["Corte", "Perfuração", "Pancada"]          # poder base: 4
    # atkMagicoMedio = ["Zionga", "Garula", "Agilao", "Bufula"] # poder base: 5

    if golpe in atkMagicoLeve: return 3
    elif golpe in atkFisicoLeve: return 4
    else: return 5

def calcularDano(poderBase, atkUsuario, acertouFraqueza=False): #* retorna o dano calculado
    dano = ((poderBase * 15) ** 0.5) * (int(atkUsuario) / 2)
    if acertouFraqueza: dano += (dano / 2)
    return int(dano)

# FUNÇÕES relacionadas às condições especiais

def maisUmOuAtaqueConjunto(sombraAlvo, idxSombraAlvo, sombras): #* str (define se é uma ação "Mais Um" ou "Ataque em Conjunto")
    temMaisUm = False

    # verificando se há apenas 1 sombra viva
    if sombraAlvo[1] < 0: # caso ela seja derrotada, nenhuma condição especial acontece e o combate encerra
        sombras = derrotarSombra(sombraAlvo, idxSombraAlvo, sombras)
    else:
        sombras[idxSombraAlvo] = sombraAlvo # atualizando a lista de sombras após DERRUBAR a atual
    
    if len(sombras) > 0:
        # verificando se ainda há pelo menos 1 sombra que NÃO FOI DERRUBADA
        for somb in sombras:
            if not somb[4] and not temMaisUm:
                temMaisUm = True
        return "maisUm" if temMaisUm else "ataqueConjunto"
    else: return "acabou o combate"

def rodarMaisUm(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno):
    print("MAIS UM!")
    print("Mitsuru: Você acertou uma fraqueza! Continue no ataque!")

    numTurno = gerarRelatorioTurno(numTurno, makotoHp, sombras)
    return turnoMakoto(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno)

def rodarAtaqueConjunto(sombras):
    print("Mitsuru: Todos os inimigos cairam! Avancem com tudo!")
    print("MASS DESTRUCTION!")
    sombras = []
    return sombras

# FUNÇÕES dos turnos de Makoto e sombras

def turnoMakoto(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno):
    dano = 0
    sombraAlvo, idxSombraAlvo = proximaSombraAlvo(sombras)

    print("Makoto: O que fazer...")
    # validando a ação
    entradaValida = False
    while not entradaValida:
        acao = input()
        if acao in ["yukari", "junpei", "persona", "atacar"]:
            entradaValida = True
            if acao == "yukari" and usosYukari == 0:
                print("Yukari: Estou exausta, foi mal!")
                entradaValida = False
            elif acao == "junpei" and usosJunpei == 0:
                print("Junpei: Cara, tô cansado!")
                entradaValida = False
            elif acao == "persona" and makotoMp < persona[3]:
                print("Makoto: Estou cansado...")
                entradaValida = False

    # AÇÃO - Persona
    if acao == "persona":
        makotoMp -= persona[3]

        listaBsort = converterLista(input().split(" "))
        qtdTrocasCres, qtdTrocasDecres = bubbleSort(listaBsort)

        if min(qtdTrocasCres, qtdTrocasDecres) > 5: #* errou
            print("Makoto: O quê?!")
            print("Mitsuru: Mais foco, Makoto!")
        else:
            poderBase = calcularPoderBase(persona[2])

            if qtdTrocasCres == 0 or qtdTrocasDecres == 0: #* acertou fraqueza
                print(f"Makoto: Venha {persona[0]}!")
                dano = calcularDano(poderBase, persona[1], True)

                sombraAlvo[1] -= dano
                sombraAlvo[4] = True
                print(f"Mitsuru: Makoto acertou {sombraAlvo[0]} causando {dano} de dano!")

                condicaoEsp = maisUmOuAtaqueConjunto(sombraAlvo, idxSombraAlvo, sombras)
                if condicaoEsp == "maisUm":
                    usosYukari, usosJunpei, makotoHp, makotoMp, sombras, numTurno = rodarMaisUm(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno)
                elif condicaoEsp == "ataqueConjunto":
                    sombras = rodarAtaqueConjunto(sombras)

            else: #* acertou normal
                print("Makoto: Persona!")
                dano = calcularDano(poderBase, persona[1])

                sombraAlvo[1] -= dano
                print(f"Mitsuru: Makoto acertou {sombraAlvo[0]} causando {dano} de dano!")
                sombras = derrotarSombra(sombraAlvo, idxSombraAlvo, sombras)

    # AÇÃO - Atacar
    elif acao == "atacar":
        dano = calcularDano(2, persona[1])
        sombraAlvo[1] -= dano
        print(f"Mitsuru: Makoto acertou {sombraAlvo[0]} causando {dano} de dano!")
        sombras = derrotarSombra(sombraAlvo, idxSombraAlvo, sombras)

    # AÇÃO - Yukari
    elif acao == "yukari":
        print("Yukari: Aguenta ai, líder!")
        print("Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado")

        makotoHp += 100
        if makotoHp > 300: makotoHp = 300

        usosYukari -= 1

    # AÇÃO - Junpei
    else:
        print("Junpei: HOOOOOME RUUUUN!!")
        print(f"Mitsuru: Acerto CRÍTICO de Junpei! {sombraAlvo[0]} sofreu 100 de dano!")
        sombraAlvo[1] -= 100
        sombraAlvo[4] = True
        usosJunpei -= 1

        condicaoEsp = maisUmOuAtaqueConjunto(sombraAlvo, idxSombraAlvo, sombras)
        if condicaoEsp == "maisUm":
            usosYukari, usosJunpei, makotoHp, makotoMp, sombras, numTurno = rodarMaisUm(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno)
        elif condicaoEsp == "ataqueConjunto":
            sombras = rodarAtaqueConjunto(sombras)

    return usosYukari, usosJunpei, makotoHp, makotoMp, sombras, numTurno
    
def turnoSombra(sombra, makotoHp):
    if sombra[4]: sombra[4] = False # se ela estiver derrubada, se levanta

    poderBase = calcularPoderBase(sombra[3])
    dano = calcularDano(poderBase, sombra[2])
    makotoHp -= dano
    print(f"Mitsuru: Makoto foi atacado por {sombra[0]} e recebeu {dano} de dano!")

    return makotoHp

# FUNÇÃO principal (exploração e combate de turnos)

def main():
    # variáveis iniciais
    andaresExplorados = 0
    numTurno = 1
    makotoHp = 300
    makotoMp = 70
    usosYukari = 2
    usosJunpei = 1
    qtdSombras = 0

    # 0: nome | 1: forcaAtaque | 2: golpe | 3: custoMp
    persona = []
    # 0: nome | 1: vida | 2: forçaAtaque | 3: golpe | 4: isDerrubada
    # quando a sombra for derrotada, será excluída da lista
    sombras = []
    idxSombra = 0

    print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")
    while makotoHp > 0: # exploração
        # input persona
        persona = converterLista(input().split(" - "))
        print(f"{persona[0]}: Eu sou tu e tu és eu...")

        # input sombras
        qtdSombras = int(input())
        for i in range(qtdSombras):
            sombInput = converterLista(input().split(" - "))
            sombInput.append(False) # isDerrubada
            sombras.append(sombInput)
        print("Mitsuru: Inimigos detectados, se preparem!")

        # combate de turnos
        while makotoHp > 0 and len(sombras) > 0:
            # turno de Makoto e atualização das variáveis utilizadas nele
            usosYukari, usosJunpei, makotoHp, makotoMp, sombras, numTurno = turnoMakoto(usosYukari, usosJunpei, makotoHp, makotoMp, persona, sombras, numTurno)
            
            # turno da sombra
            if len(sombras) > 0:
                # caso passe dos limites da lista de sombras, o programa volta do início
                if (idxSombra + 1) > len(sombras): idxSombra = 0
                makotoHp = turnoSombra(sombras[idxSombra], makotoHp)
                # se a lista tiver mais de 1 sombra, avança mais uma posição pro próximo turno
                if len(sombras) > 1: idxSombra += 1
                
                if makotoHp > 0: # se Makoto estiver vivo
                    # relatório do turno
                    numTurno = gerarRelatorioTurno(numTurno, makotoHp, sombras)
            # todas as sombras foram derrotadas
            else:
                print("Mitsuru: Muito bem! Continuem a exploração.")
                # reseta e atualiza as variáveis necessárias
                andaresExplorados += 1
                usosYukari = 2
                usosJunpei = 1

                makotoHp += 50
                if makotoHp > 300: makotoHp = 300
                makotoMp += 15
                if makotoMp > 70: makotoMp = 70

                numTurno = 1

    print("Makoto: Argh...")
    print("Mitsuru: Líder? Aconteceu algo? Responda!")
    print()
    print("FIM DE JOGO")
    print(f"Andares explorados: {andaresExplorados}")

main()