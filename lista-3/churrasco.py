qtdConvidados = int(input())

matrizConvidados = [] # [[nome1, alimento1, preço1], [nome2, alimento2, preço2], ...]
listaAux = [] # lista auxiliar

nomeConvidado = ""
alimento = ""
precoAlimento = 0

# preenchendo a matriz de convidados
for i in range(qtdConvidados):
    nomeConvidado = input()
    alimento = input()
    precoAlimento = int(input())

    if nomeConvidado == "Maicon Kuster": print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        # lista os alimentos já cadastrados
        for j in range(len(matrizConvidados)):
            listaAux.append(matrizConvidados[j][1])

        # verifica se o alimento cadastrado é igual a outro já existente
        if listaAux.count(alimento) > 0: print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nomeConvidado}")
        else:
            listaAux = []
            listaAux.append(nomeConvidado)
            listaAux.append(alimento)
            listaAux.append(precoAlimento)
            matrizConvidados.append(listaAux[:])
            listaAux = []

if len(matrizConvidados) == 0: print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    # Bubble Sort para ordenar a lista tanto pelo preço da comida como pelo nome

    for i in range(len(matrizConvidados) - 1):
        for j in range(len(matrizConvidados) - i - 1):
            # ordenando pelo preço
            if matrizConvidados[j][2] > matrizConvidados[j + 1][2]:
                listaAux = matrizConvidados[j + 1]
                matrizConvidados[j + 1] = matrizConvidados[j]
                matrizConvidados[j] = listaAux
            # ordenando pelo nome
            elif matrizConvidados[j][2] == matrizConvidados[j + 1][2]:
                listaAux = sorted(matrizConvidados[j:j + 2]) # "sorted()" ordena as listas em ordem alfabética
                for k in range(2):
                    matrizConvidados[j + k] = listaAux[k]

    print(f"Obrigado para o(a) {matrizConvidados[len(matrizConvidados) - 1][0]} pelo(a) excelente {matrizConvidados[len(matrizConvidados) - 1][1]}")
    if len(matrizConvidados) > 1:
        print(f"Rapaz, {matrizConvidados[0][0]} trouxe o(a) {matrizConvidados[0][1]} que estava altamente mais ou menos!!!")

    print("Lista de convidados do Calabreso")
    for i in range(len(matrizConvidados)):
        print(f"{i + 1}- {matrizConvidados[i][0]}")

    listaAux = []