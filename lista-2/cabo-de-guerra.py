print("Começa agora o treinamento para grande final mundial de cabo de guerra!")

# quantidade de partidas
qtdPartidas = int(input())
while qtdPartidas % 2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    qtdPartidas = int(input())
print(f"Eles batalharão em {qtdPartidas} longas partidas.")

# forças
forcaArthur = int(input())
forcaJoao = int(input())
maisForte = ""
maisFraco = ""
if forcaArthur > forcaJoao:
    maisForte = "Arthur"
    maisFraco = "João"
else:
    maisForte = "João"
    maisFraco = "Arthur"

# resistências
resistencia = int(input())
resArthur = resistencia
resJoao = resistencia

# pontos
ptsArthur = 0
ptsJoao = 0

# outras informações da competição
numRodada = 0
isPrimo = True
semVirada = False

# mistura de while com for para que a competição também termine caso não tenha chance de virada
i = 0
while not semVirada and i < qtdPartidas:
    print(f"Começa a {i + 1}ª partida!")
    print(f"Placar geral: {ptsArthur} X {ptsJoao}")

    resArthur = resistencia
    resJoao = resistencia
    
    while resArthur > 0 and resJoao > 0:
        isPrimo = True
        numRodada = int(input())

        # verificando se o número da rodada é primo
        if numRodada % 2 == 0 and numRodada > 2: isPrimo = False
        else:
            for j in range(2, numRodada // 2):
                if numRodada % j == 0 and isPrimo:
                    isPrimo = False

        # gambiarra para saber se é quadrado perfeito
        if (numRodada ** 0.5) - int(numRodada ** 0.5) == 0: # Arthur ganhou
            resArthur += 1
            resJoao -=1
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
        elif isPrimo: # João ganhou
            resJoao += 1
            resArthur -= 1
            print("O primo do primo é primo do primo? João puxa mais forte!")
        else: # mais forte ganhou
            if maisForte == "Arthur":
                resArthur += 1
                resJoao -= 1
            else:
                resJoao += 1
                resArthur -= 1
            print(f"{maisForte} é o mais forte! {maisFraco} não consegue segurar.")
        
    if resJoao == 0:
        ptsArthur += 1
        print("Arthur dá orgulho para Maceió e ganha a partida!")
    else:
        ptsJoao += 1
        print("João usa seus talentos de mangueboy e leva essa para casa!")

    # verificação para ver se uma virada ainda é possível
    if ptsArthur > (qtdPartidas / 2) or ptsJoao > (qtdPartidas / 2):
        semVirada = True
    
    i += 1

print("\nAgora eles estão prontos para o mundial!")
print(f"Placar final: {ptsArthur} X {ptsJoao}")

if ptsArthur == 0:
    print("Arthur não teve chance! João venceu todas as partidas.")
elif ptsJoao == 0:
    print("João não teve chance! Arthur venceu todas as partidas.")
elif ptsArthur > ptsJoao:
    print(f"O ganhador foi Arthur com uma diferença de {ptsArthur - ptsJoao} partidas.")
else:
    print(f"O ganhador foi João com uma diferença de {ptsJoao - ptsArthur} partidas.")