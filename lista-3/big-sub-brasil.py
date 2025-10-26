print("Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")

participantes = input()
listParticipantes = [parti.capitalize() for parti in participantes.split(", ")]
print(f"{listParticipantes[0]} e {listParticipantes[1]} disputarão entre si.")

listNumInput = []
listMaior = []
listMenor = []
listConsequentes = []
matriz = []

listPontuacao = []
listNumEmpate = []
vencedor = ""

for i in range(2):
    numeros = input()
    listNumInput = numeros.split(" ")
    listNumInput = [int(num) for num in listNumInput]
    listNumInput.sort()

    listMaior = listNumInput[7:10] # maiores números
    listMenor = listNumInput[0:3] # menores números
    listConsequentes = [num + 1 for num in listNumInput[3:6]] # consequentes dos 3 primeiros restantes
    listNumEmpate.append(listNumInput[6]) # número para desempate que sobrou

    matriz = [listMaior, listMenor, listConsequentes]

    # determinante
    diagonalPrincipal = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
    diagonalSecundaria = -(matriz[2][0] * matriz[1][1] * matriz[0][2]) - (matriz[2][1] * matriz[1][2] * matriz[0][0]) - (matriz[2][2] * matriz[1][0] * matriz[0][1])
    listPontuacao.append(diagonalPrincipal + diagonalSecundaria)
    
    # imprimindo
    for j in range(3):
        matriz[j] = [str(num) for num in matriz[j]]
        print(" ".join(matriz[j]))
    print(f"{listParticipantes[i]} está com pontuação {listPontuacao[i]} pontos.")

    matriz = []

if listPontuacao[0] > listPontuacao[1]:
    vencedor = listParticipantes[0]
elif listPontuacao[1] > listPontuacao[0]:
    vencedor = listParticipantes[1]
else:
    print("RODADA DESEMPATE!!")
    if listNumEmpate[0] > listNumEmpate[1]:
        vencedor = listParticipantes[0]
    elif listNumEmpate[1] > listNumEmpate[0]:
        vencedor = listParticipantes[1]
    
    if len(vencedor) > 0:
        print(f"Contra todas as expectativas (inclusive as nossas), {vencedor} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {listParticipantes[0] if listParticipantes[1] == vencedor else listParticipantes[1]}. Melhor sorte no próximo flop!")
    else:
        print("Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")

if len(vencedor) > 0: print(f"Com talento duvidoso e esforço máximo, a vitória é de {vencedor}!")