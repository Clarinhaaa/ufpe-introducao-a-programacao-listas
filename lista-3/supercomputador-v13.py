# projetos
listNomesProjeto = []
listQtdProjeto = []

# inputs
nomeProjeto = input()
inputStringItem = ""

# variáveis para o item da vez
nomeItem = ""
qtdItem = 0

# itens ÚTEIS
listNomesItensUteis = []
listQtdItensUteis = []
# itens INÚTEIS
matrizItensInuteis = []

matrizItensFaltantes = []

construiu = False

# especificações de cada projeto
if nomeProjeto == "Memória ROM Simples":
    listNomesProjeto = ["Redstone", "Repetidores", "Tochas de Redstone"]
    listQtdProjeto = [256, 64, 128]
elif nomeProjeto == "Calculadora de 4 bits":
    listNomesProjeto = ["Redstone", "Repetidores", "Tochas de Redstone", "Lâmpadas de Redstone"]
    listQtdProjeto = [512, 128, 64, 256]
elif nomeProjeto == "Sequenciador Musical":
    listNomesProjeto = ["Redstone", "Repetidores", "Blocos de Notas", "Observadores"]
    listQtdProjeto = [1024, 256, 64, 128]
elif nomeProjeto == "Processador de 8 Bits":
    listNomesProjeto = ["Redstone", "Repetidores", "Lâmpadas de Redstone", "Pistões Aderentes"]
    listQtdProjeto = [4096, 1024, 2048, 512]
elif nomeProjeto == "Display de Vídeo 8x8":
    listNomesProjeto = ["Redstone", "Repetidores", "Comparadores", "Pistões"]
    listQtdProjeto = [2048, 512, 256, 128]
else: # "Supercomputador V13"
    listNomesProjeto = ["Redstone", "Repetidores", "Comparadores", "Pistões Aderentes"]
    listQtdProjeto = [8192, 2048, 1024, 1024]

while not construiu:
    inputStringItem = input()
    while inputStringItem != "Construir!":
        # dividir nome e quantidade em duas variáveis diferentes
        i = 0
        dividiu = False
        while not dividiu:
            if inputStringItem[i] in "0123456789":
                nomeItem = inputStringItem[0:i - 1]
                qtdItem = int(inputStringItem[i:len(inputStringItem)])
                dividiu = True
            i += 1

        if nomeItem in listNomesProjeto:
            if nomeItem not in listNomesItensUteis:
                listNomesItensUteis.append(nomeItem)
                listQtdItensUteis.append(qtdItem)
            else:
                listQtdItensUteis[listNomesItensUteis.index(nomeItem)] += qtdItem
            
            if nomeItem == "Redstone":
                print(f"Mais redstone! A energia que move o progresso! (+{qtdItem} Redstone)")
            elif nomeItem == "Repetidores":
                print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{qtdItem} Repetidores)")
            elif nomeItem == "Tochas de Redstone":
                print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{qtdItem} Tochas de Redstone)")
            elif nomeItem == "Lâmpadas de Redstone":
                print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{qtdItem} Lâmpadas de Redstone)")
            elif nomeItem == "Blocos de Notas":
                print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{qtdItem} Blocos de Notas)")
            elif nomeItem == "Observadores":
                print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{qtdItem} Observadores)")
            elif nomeItem == "Comparadores":
                print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{qtdItem} Comparadores)")
            elif nomeItem == "Pistões":
                print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{qtdItem} Pistões)")
            else:
                print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{qtdItem} Pistões Aderentes)")
        else:
            print(f"Hmm, {nomeItem} não parece ser útil para este projeto.")
            matrizItensInuteis.append([nomeItem, qtdItem])

        inputStringItem = input()
    print() # quebra de linha

    if len(listNomesItensUteis) == len(listNomesProjeto):
        construiu = True
        i = 0
        while construiu and i < len(listQtdProjeto):
            if listQtdProjeto[i] > listQtdItensUteis[listNomesItensUteis.index(listNomesProjeto[i])]: construiu = False
            i += 1

    if construiu:
        print(f"Viniccius13 conseguiu construir o {nomeProjeto}! Partiu programar!\n")

        print(f"Para construirmos a(o) {nomeProjeto}, utilizamos:\n")
        for i in range(len(listNomesItensUteis)):
            print(f"{listNomesItensUteis[i]} : {listQtdItensUteis[i]}")

        if len(matrizItensInuteis) > 0:
            print("\nMas, em nossa jornada, também coletamos:\n")
            for i in range(len(matrizItensInuteis)):
                print(f"{matrizItensInuteis[i][0]} : {matrizItensInuteis[i][1]}")
    else: # not construiu
        inputStringItem = ""

        print(f"Ainda não é possível construir o {nomeProjeto}! Faltam:\n")

        for i in range(len(listNomesProjeto)):
            if listNomesProjeto[i] not in listNomesItensUteis:
                print(f"{listQtdProjeto[i] // 64} pack(s) de {listNomesProjeto[i]}")
            else:
                qtdItensUteisAtual = listQtdItensUteis[listNomesItensUteis.index(listNomesProjeto[i])]
                if listQtdProjeto[i] > qtdItensUteisAtual:
                    packsRestantes = 1 if (listQtdProjeto[i] - qtdItensUteisAtual) // 64 == 0 else (listQtdProjeto[i] - qtdItensUteisAtual) // 64
                    print(f"{packsRestantes} pack(s) de {listNomesProjeto[i]}")

        print() # quebra de linha