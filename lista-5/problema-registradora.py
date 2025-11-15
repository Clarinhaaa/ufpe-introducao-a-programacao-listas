# - tentativa de pesquisa por profundidade com uma simulação de grafo
# - os vértices "raizes" serão as notas e, a partir de cada uma, serão verificadas possibilidades
# de combinações que, quando subtraídas com o valor da conta, chegue a 0

def calcularPossibilidades(valorConta, notas, listaComb, listaTotalComb):
    if valorConta % 5 != 0:
        return []
    
    if valorConta == 0:
        return [[]]
    
    if valorConta == 5:
        return [[5]]
    
    # função separada para a pesquisa, para que a calcularPossibilidades retorne apenas a lista total de combinações para UMA nota
    # verificando se a diferença do valor com a nota atual é maior, menor ou igual a 0
    # a recursão consiste na subtração desse valor pelas notas que formem as combinações possíveis, até que chegue a 0
    def pesquisaProfundidade(difValor, idxNotaAtual):
        # se for positivo, cotinua a busca
        if difValor > 0:
            listaComb.append(notas[idxNotaAtual])
            for i in range(idxNotaAtual, len(notas)):
                pesquisaProfundidade(difValor - notas[i], i)
            listaComb.pop()
        # se for negativo, volta uma posição no "grafo"
        elif difValor < 0:
            return
        # se for igual, atualiza a lista de combinações totais
        else:
            listaComb.append(notas[idxNotaAtual])
            # "listaComb.copy()" para que seu valor não seja armazenado em todas as mesmas instâncias de listaComb em listaTotalComb
            listaTotalComb.append(listaComb.copy())
            listaComb.pop()
        return

    # loop que percorre todas as possibilidades para todas as notas
    for i in range(len(notas)):
        pesquisaProfundidade(valorConta - notas[i], i)

    return listaTotalComb

def main():
    valorConta = int(input())
    notas = [100, 50, 20, 10, 5]
    combinacoes = []
    listaQtdNotas = [0, 0, 0, 0, 0]

    print(f"Calculando possibilidades para o valor: {valorConta}")

    combinacoes = calcularPossibilidades(valorConta, notas, [], [])

    if len(combinacoes) == 0:
        print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")
    else:
        if len(combinacoes) == 1:
            print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
            if len(combinacoes[0]) > 0: listaQtdNotas = [0, 0, 0, 0, 1]
        else:
            # contando quantas vezes cada nota aparece em cada combinação encontrada
            for i in range(len(combinacoes)):
                for j in range(len(combinacoes[i])):
                    if combinacoes[i][j] == 100:
                        listaQtdNotas[0] += 1
                    elif combinacoes[i][j] == 50:
                        listaQtdNotas[1] += 1
                    elif combinacoes[i][j] == 20:
                        listaQtdNotas[2] += 1
                    elif combinacoes[i][j] == 10:
                        listaQtdNotas[3] += 1
                    else: # combinacoes[i][j] == 5
                        listaQtdNotas[4] += 1

    print(f"\nTotal de possibilidades: {len(combinacoes)}")
    print("\nUso das notas:")
    for i in range(len(notas)):
        print(f"R${notas[i]}: usada em {listaQtdNotas[i]} combinações")
        
main()