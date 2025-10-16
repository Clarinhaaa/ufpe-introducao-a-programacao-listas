print("--- Simulador de Cancelamento ---\n")

qtdArtistas = int(input())
stringArtistas = ""
matrizArtistas = []
evento = 0

for i in range(qtdArtistas):
    stringArtistas = input()
    matrizArtistas.append(stringArtistas.split(" - "))
    matrizArtistas[i][1] = int(matrizArtistas[i][1])

for i in range(len(matrizArtistas)):
    print(f"A subcelebridade da vez é: {matrizArtistas[i][0]}")

    evento = int(input())
    if evento == 1:
        print(f"{matrizArtistas[i][0]} perdeu 10% dos seguidores!")
        matrizArtistas[i][1] -= matrizArtistas[i][1] // 10
    elif evento == 2:
        print(f"{matrizArtistas[i][0]} ganhou 5% de seguidores!")
        matrizArtistas[i][1] += matrizArtistas[i][1] // 20
    elif evento == 3:
        print(f"{matrizArtistas[i][0]} perdeu 15% dos seguidores!")
        matrizArtistas[i][1] -= (matrizArtistas[i][1] * 15) // 100
    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

# Bubble Sort decrescente
listAux = []
for i in range(len(matrizArtistas) - 1):
    for j in range(len(matrizArtistas) - i - 1):
        if matrizArtistas[j][1] < matrizArtistas[j + 1][1]:
            listAux = matrizArtistas[j + 1]
            matrizArtistas[j + 1] = matrizArtistas[j]
            matrizArtistas[j] = listAux

print("\n--- RANKING FINAL DE SEGUIDORES ---")
rangePersonalizada = range(3) if len(matrizArtistas) >= 3 else range(len(matrizArtistas))
for i in rangePersonalizada:
    print(f"{i + 1}º Lugar: {matrizArtistas[i][0]} com {matrizArtistas[i][1]} seguidores.")