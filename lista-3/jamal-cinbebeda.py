print("Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…")
print('Jamal - "Que danado é isso?"')

inputMonitores = input()
inputValido = False
matrizMonitores = []
listaMonitoresValidos = ["Guilherme", "Henrique", "Júnior", "Miguel"]

# verificação da entrada inputMonitores
while not inputValido:
    inputValido = True
    matrizMonitores = []
    nomes = []

    listaInput = inputMonitores.split(", ")
    for i in range(0, len(listaInput) - 1, 2):
        matrizMonitores.append([listaInput[i], int(listaInput[i + 1])])
        nomes.append(listaInput[i])

    for i in range(len(listaMonitoresValidos)):
        if listaMonitoresValidos[i] not in nomes and inputValido:
            inputValido = False
    if not inputValido:
        print("Insira nomes válidos.")
        inputMonitores = input()

# verifica nota 10
for i in range(len(matrizMonitores)):
    if matrizMonitores[i][1] == 10:
        print(f"O monitor {matrizMonitores[i][0]} é diferenciado! Teve a aprovação do próprio Jamal.")

matrizPassos = [[".", ".", "."],
                [".", ".", "."],
                ["E", ".", "D"]]
pe = ""
peAnterior = ""
iPasso = -1
jPasso = -1
qtdErros = 0
aprendeu = False
segundaChance = False
qtdTentativas = 1

primeiroMovimentoInvalido = False

# ordena os monitores da menor para a maior nota
for i in range(len(matrizMonitores) - 1):
    for j in range(len(matrizMonitores) - i - 1):
        if matrizMonitores[j][1] > matrizMonitores[j+1][1]:
            listaAux = matrizMonitores[j]
            matrizMonitores[j] = matrizMonitores[j+1]
            matrizMonitores[j+1] = listaAux
monitorMenorNota = matrizMonitores[0][0]
print(f"Jamal avaliou a situação dos monitores e viu que {monitorMenorNota} é o mais necessitado.")

# MOVIMENTOS DO JAMAL
# primeira matriz padrão
listaPassosJamal = ["D12", "D33", "E12", "E31", "D12", "E31", "D12"]
print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."')
print()
print("Jamal - Movimentação 0:")
for i in range(len(matrizPassos)):
    print(" ".join(matrizPassos[i]))

# manipulação da matriz de acordo com os passos
for i in range(len(listaPassosJamal)):
    passo = listaPassosJamal[i]
    pe = passo[0]
    iPasso = int(passo[1]) - 1
    jPasso = int(passo[2]) - 1

    for j in range(len(matrizPassos)):
            if pe in matrizPassos[j]: matrizPassos[j][matrizPassos[j].index(pe)] = "."
            if str(i) in matrizPassos[j]:
                if pe != peAnterior:
                    if pe == "E":
                        matrizPassos[j][matrizPassos[j].index(str(i))] = "D"
                    if pe == "D":
                        matrizPassos[j][matrizPassos[j].index(str(i))] = "E"
                else:
                    matrizPassos[j][matrizPassos[j].index(str(i))] = "."
    
    peAnterior = passo[0]
    matrizPassos[iPasso][jPasso] = str(i + 1)

    print()
    print(f"Jamal - Movimentação {i + 1}:")
    for j in range(len(matrizPassos)):
        print(" ".join(matrizPassos[j]))

# MOVIMENTOS DO MONITOR
while not aprendeu and qtdTentativas < 3:
    inputPassos = input()
    inputValido = False

    # verificando a validez dessa entrada
    while not inputValido:
        inputValido = True
        listaPassosMonitor = inputPassos.split(", ")
        if len(listaPassosMonitor) == 7:
            for passo in listaPassosMonitor:
                if ((passo[0] not in "ED") or (passo[1] not in "123") or (passo[2] not in "123")) and inputValido:
                    inputValido = False
        else: inputValido = False

        if not inputValido:
            if not primeiroMovimentoInvalido:
                print()
                primeiroMovimentoInvalido = True
            print("Movimento inválido! Por favor, insira outro.")
            inputPassos = input()

    matrizPassos = [[".", ".", "."],
                    [".", ".", "."],
                    ["E", ".", "D"]]
    qtdErros = 0

    # primeira matriz padrão
    print()
    print(f"{monitorMenorNota} - Movimentação 0:")
    for i in range(len(matrizPassos)):
        print(" ".join(matrizPassos[i]))

    # manipulação da matriz de acordo com os passos
    for i in range(len(listaPassosMonitor)):
        passo = listaPassosMonitor[i]
        pe = passo[0]
        iPasso = int(passo[1]) - 1
        jPasso = int(passo[2]) - 1

        for j in range(len(matrizPassos)):
            if pe in matrizPassos[j]: matrizPassos[j][matrizPassos[j].index(pe)] = "."
            if str(i) in matrizPassos[j]:
                if pe != peAnterior:
                    if pe == "E":
                        matrizPassos[j][matrizPassos[j].index(str(i))] = "D"
                    if pe == "D":
                        matrizPassos[j][matrizPassos[j].index(str(i))] = "E"
                else:
                    matrizPassos[j][matrizPassos[j].index(str(i))] = "."

        # conta os erros do monitor
        if listaPassosMonitor[i] != listaPassosJamal[i]: qtdErros += 1

        peAnterior = passo[0]
        matrizPassos[iPasso][jPasso] = str(i + 1)
        print()
        print(f"{monitorMenorNota} - Movimentação {i + 1}:")
        for j in range(len(matrizPassos)):
            print(" ".join(matrizPassos[j]))

    if qtdErros == 0: aprendeu = True
    elif qtdErros == 1:
        if qtdTentativas == 1:
            print()
            print("Foi quase! O monitor merece uma nova chance!")
            segundaChance = True
        qtdTentativas += 1
    else: # qtdErros >= 2
        qtdTentativas = 4
            
print()
if aprendeu:
    if not segundaChance:
        if monitorMenorNota == "Júnior":
            print("Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.")
        elif monitorMenorNota == "Henrique":
            print("O maldito talento ataca novamente! Tinha que ser o desenrolado.")
        elif monitorMenorNota == "Miguel":
            print("O cara veio do interior pra mostrar como que se faz!")
        else: # Guilherme
            print("Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.")
    else:    
        print(f"Era isso! {monitorMenorNota} só estava precisando de um empurrãozinho.")

    print('Jamal - "Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!"')
    respostaConvite = input()
    if respostaConvite == "Sim":
        print(f"Óbvio que o monitor {monitorMenorNota} não perderia essa oportunidade por nada!")
    else: # Não
        print(f"Infelizmente o monitor {monitorMenorNota} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.")
else:
    if not segundaChance:
        if qtdErros == 2:
                print(f"Melhor o monitor {monitorMenorNota} deixar esse negócio de dança pra lá.")
        elif qtdErros == 3:
                print("Isso tá horrível!")
        else:
                print(f"O monitor {monitorMenorNota} foi expulso da festa por não saber dançar.")
    else:
        print(f"Nem com outra tentativa {monitorMenorNota} conseguiu ajeitar isso.")
    
    print("Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.")