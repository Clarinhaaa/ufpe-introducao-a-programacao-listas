linhaInput = ""
listStrInput = []
listIntInput = []
matrizSudoku = []

iAux = 0
jAux = 0
iAnterior = 0
jAnterior = 0

linha = True
coluna = True
quadrado = True
backtrack = False
achouSolucaoNum = False
achouSolucaoTotal = False

# preenche a matriz
# transforma a string de entrada em inteiros, substituíndo o "." por "0", para indicar espaços vazios
for i in range(9):
    linhaInput = input().replace(".", "0")
    listStrInput = linhaInput.split()
    listIntInput = [int(num) for num in listStrInput]
    matrizSudoku.append(listIntInput)

# resolve o sudoku
while not achouSolucaoTotal:
    # se o espaço for "vazio" ou não, mas que vem de um backtrack para a última casa modificada
    if matrizSudoku[iAux][jAux] == 0 or backtrack:
        matrizSudoku[iAux][jAux] = 1
        achouSolucaoNum = False

        # testa os valores de 1 a 9 para cada espaço vazio na matriz
        while not achouSolucaoNum:
            linha = True
            coluna = True
            quadrado = True

            if backtrack:
                iAux = iAnterior
                jAux = jAnterior
                matrizSudoku[iAux][jAux] += 1
                backtrack = False

            # verifica se é o único na linha
            if matrizSudoku[iAux].count(matrizSudoku[iAux][jAux]) > 1: linha = False
            # verifica se é o único na coluna
            for i in range(9):
                if i != iAux and matrizSudoku[i][jAux] == matrizSudoku[iAux][jAux] and coluna:
                    coluna = False
            # verifica se é o único no quadrado 3x3 no qual se localiza
            if iAux >= 0 and iAux < 3: i = 0
            elif iAux >= 3 and iAux < 6: i = 3
            else: i = 5

            if jAux >= 0 and jAux < 3: j = 0
            elif jAux >= 3 and jAux < 6: j = 3
            else: j = 5

            count1 = matrizSudoku[i][j:j+3].count(matrizSudoku[iAux][jAux])
            count2 = matrizSudoku[i+1][j:j+3].count(matrizSudoku[iAux][jAux])
            count3 = matrizSudoku[i+2][j:j+3].count(matrizSudoku[iAux][jAux])
            qtdNumQuadrado = count1 + count2 + count3

            if qtdNumQuadrado > 1: quadrado = False
            
            # se o número de matriz[iAux][jAux] for inválido, ele é incrementado
            # caso contrário, vai para o próximo espaço vazio da matriz
            if not linha or not coluna or not quadrado:
                matrizSudoku[iAux][jAux] += 1
                # verifica se todos os números possíveis (1 a 9) foram testados e não deram certo
                if matrizSudoku[iAux][jAux] > 9:
                    backtrack = True
                    matrizSudoku[iAux][jAux] = 0
            else:
                achouSolucaoNum = True
                iAnterior = iAux
                jAnterior = jAux

    else: # se o espaço não for "vazio" e não for um backtrack, anda mais uma casa
        jAux += 1
        if jAux >= 9:
            iAux += 1
            jAux = 0

# imprime a matriz
print()
for i in range(9):
    matrizSudoku[i] = [str(num) for num in matrizSudoku[i]]
    print(" ".join(matrizSudoku[i]))