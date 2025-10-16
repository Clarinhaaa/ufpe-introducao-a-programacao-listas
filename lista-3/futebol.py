print("RECEBA! É hoje que eu me torno o melhor dos melhores.")

# inputs
qtdTreinos = int(input())
habilidadeInicial = int(input())
sequenciaTreinosGoleiros = input()

# goleiros e treinos
goleirosEspeciais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]
habilidadeGoleiro = -1
meta = (100 - habilidadeInicial) / qtdTreinos
ptsTreino = 0

# listas
listSequencia = sequenciaTreinosGoleiros.split("-")
listBatidas = []
listGoleiros = []
matriz = []
xLuva = -1
yLuva = -1
isGol = True

# outputs iniciais
if habilidadeInicial <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")
elif habilidadeInicial >= 6 and habilidadeInicial <= 15: 
    print("Não tem jeito, vou ser o melhor do mundo!")
else:
    print("O Pai tá estourado! RECEBA!")

print(f"Meta por Partida: {meta}")

# preenchendo as listas de batidas e goleiros separadamente
for i in range(len(listSequencia)):
    if i % 2 == 0: listBatidas.append(listSequencia[i])
    else: listGoleiros.append(listSequencia[i])

i = 0
while i < qtdTreinos and habilidadeInicial <= 100:
    ptsTreino = 0
    isGol = True
    print(f"TIPO DE PARTIDA: {listBatidas[i]}")
    print(f"Nome do Goleiro: {listGoleiros[i]}")

    if listGoleiros[i] not in goleirosEspeciais:
        habilidadeGoleiro = int(input())
    
    matriz = eval(input())
    xLuva = int(input())
    yLuva = int(input())

    if matriz[xLuva][yLuva] == 1:
        if listGoleiros[i] not in goleirosEspeciais:
            if habilidadeInicial > habilidadeGoleiro:
                ptsTreino += habilidadeInicial - habilidadeGoleiro
        else:
            if listGoleiros[i] == goleirosEspeciais[0]:
                print("Aí não dá, impossível de fazer gol no maior do mundo.")
                isGol = False
            elif listGoleiros[i] == goleirosEspeciais[1]:
                print("REBECA? Is that you?\nIspidi mai friand, recieve!")
                ptsTreino += meta * 1.5
            elif listGoleiros[i] == goleirosEspeciais[2]:
                print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
                if "Pênalti" in listBatidas[i]: ptsTreino += meta
                else: isGol = False
            elif listGoleiros[i] == goleirosEspeciais[3]:
                print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
                ptsTreino += meta / 2
            else:
                print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
                ptsTreino += meta * 2
    else: isGol = False

    if isGol: print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
    else: print("A jornada ainda não acabou!")

    habilidadeInicial += ptsTreino

    if habilidadeInicial <= 100:
        if ptsTreino >= meta: print(f"VAMO! PARTIDA {i + 1} DE {qtdTreinos}!")
        else: print("Dá pra recuperar depois! Vamo seguindo!")

    i += 1

if habilidadeInicial > 100:
    print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
elif habilidadeInicial == 100:
    print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")
else:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")