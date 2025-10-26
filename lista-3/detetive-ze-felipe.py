print("Iniciando investigação... Zé Felipe está focado.")

qtdEventos = int(input())
matrizEventos = [] # [["sigla", "evento", "horaInicio", "horaFim"], [...], ...]
listHoraInicio = []
listHoraFim = []
listAux = []
aux = 0.0

nivelSus = 0
vjm = False
qtdEncSus = 0
qtdAlibi = 0
nomePessoa = ""

# input dos eventos
for i in range(qtdEventos):
    strEvento = input()
    matrizEventos.append(strEvento.split(" - "))
    # verificando se o evento VJM existe na lista
    if matrizEventos[i][0] == "VJM" and not vjm:
        vjm = True
        nivelSus = 100
    # armazenando as horas de início e fim em duas listas como floats
    listHoraInicio.append(float(matrizEventos[i][2].replace(":", ".")))
    listHoraFim.append(float(matrizEventos[i][3].replace(":", ".")))

if not vjm:
    # ordenação dos eventos
    for i in range(len(matrizEventos) - 1):
        for j in range (len(matrizEventos) - i - 1):
            if listHoraInicio[j] > listHoraInicio[j + 1]:
                listAux = matrizEventos[j]
                matrizEventos[j] = matrizEventos[j + 1]
                matrizEventos[j + 1] = listAux

                aux = listHoraInicio[j]
                listHoraInicio[j] = listHoraInicio[j + 1]
                listHoraInicio[j + 1] = aux
                
                aux = listHoraFim[j]
                listHoraFim[j] = listHoraFim[j + 1]
                listHoraFim[j + 1] = aux
            elif listHoraInicio[j] == listHoraInicio[j + 1]:
                if listHoraFim[j] > listHoraFim[j + 1]:
                    listAux = matrizEventos[j]
                    matrizEventos[j] = matrizEventos[j + 1]
                    matrizEventos[j + 1] = listAux

                    aux = listHoraFim[j]
                    listHoraFim[j] = listHoraFim[j + 1]
                    listHoraFim[j + 1] = aux
                
    listAux = []
    # cálculo da suspeita
    for i in range(len(matrizEventos) - 1):
        for j in range(i + 1, len(matrizEventos)):
            # mesmo local do evento
            if matrizEventos[i][1] == matrizEventos[j][1]:
                # horários se sobrepõem
                if listHoraInicio[i] < listHoraFim[j] and listHoraInicio[j] < listHoraFim[i]:
                    # Armazenando as siglas das pessoas em uma lista para a verificação seguinte
                    listAux.append(matrizEventos[i][0])
                    listAux.append(matrizEventos[j][0])
                    if "V" in listAux and "JM" in listAux: # Encontro suspeito
                        nivelSus += 35
                        qtdEncSus += 1
                    elif "V" in listAux and "ZF" in listAux: # Álibi perfeito
                        nivelSus -= 20
                        qtdAlibi += 1
                        if nivelSus < 0: nivelSus = 0
                    listAux = []
    
print()
if nivelSus >= 100 or vjm:
    print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
else:
    print("--- Linha do Tempo dos Eventos ---")
    for i in range(len(matrizEventos)):
        if matrizEventos[i][0] == "V":
            nomePessoa = "Virgínia"
        elif matrizEventos[i][0] == "JM":
            nomePessoa = "Jogador Misterioso"
        else:
            nomePessoa = "Zé Felipe"
        print(f"{matrizEventos[i][2]}-{matrizEventos[i][3]}: {nomePessoa} - {matrizEventos[i][1]}")
    
    print("\n--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {qtdEncSus}")
    print(f"Álibis Confirmados: {qtdAlibi}")
    
    print()
    if nivelSus >= 70:
        print(f"Nível de Suspeita: {nivelSus} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
    elif nivelSus < 70 and nivelSus >= 30:
        print(f"Nível de Suspeita: {nivelSus} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
    else:
        print(f"Nível de Suspeita: {nivelSus} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")