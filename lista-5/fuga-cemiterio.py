# função que verifica se nenhum fantasma entra em conflito com a posição que está sendo analisada

# ele verifica, a cada linha ACIMA do i atual, se as posições da coluna e diagonais que partem do
# túmulo atual estão ocupadas (ou seja, tem valor 1). Se nenhuma tiver valor 1, está seguro para
# colocar um fantasma lá
def tumuloSeguro(matriz, i, j, n): # retorna um boolean
    jEsq = j - 1
    jDir = j + 1
    i -= 1

    while i >= 0:
        # também é feita a verificação para os j das diagonais não saírem dos limites da matriz
        if (matriz[i][j] == 1) or (jEsq >= 0 and matriz[i][jEsq] == 1) or (jDir < n and matriz[i][jDir] == 1):
            return False
        i -= 1
        jEsq -= 1
        jDir += 1
    
    return True

def nFantasmas(matriz, i, n):
    # caso base: chegou no final da matriz, ou seja, posicionou corretamente todos os fantasmas
    if i == n:
        return 1
    # caso recursivo: a função vai tratar de todas as possibilidades de posicionar
    # corretamente um fantasma em cada linha da matriz
    else:
        qtdPos = 0
        # já o for loop dentro dela vai iterar em todas as colunas dessa linha, verificando
        # se o túmulo é seguro antes de colocar um fantasma e passar para a próxima linha
        for j in range(n):
            if matriz[i][j] < 2: # se o túmulo analisado NÃO estiver com o selo de proteção
                if tumuloSeguro(matriz, i, j, n):
                    matriz[i][j] = 1
                    qtdPos += nFantasmas(matriz, i + 1, n) # atualiza o valor de qtdPos na volta das recursões
                    matriz[i][j] = 0

    return qtdPos

def main():
    qtdFantasmas = int(input())
    iOcupado = int(input())
    jOcupado = int(input())

    # verificação da entrada válida para o túmulo protegido
    while (iOcupado <= 0 or iOcupado > qtdFantasmas) or (jOcupado <= 0 or jOcupado > qtdFantasmas):
        print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({iOcupado}, {jOcupado}). Assim eles nunca vão conseguir sair do cemitério!")
        iOcupado = int(input())
        jOcupado = int(input())
    print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({iOcupado}, {jOcupado})!")

    # preenchendo a matriz do cemitério
    cemiterio = []
    for i in range(qtdFantasmas):
        # os túmulos com valor 0 estão livres
        # e quando forem ocupados por um fantasma, terão valor 1
        cemiterio.append([0 for j in range(qtdFantasmas)])
    cemiterio[iOcupado - 1][jOcupado - 1] = 2 # o túmulo protegido tem valor 2 na matriz

    qtdPos = nFantasmas(cemiterio, 0, qtdFantasmas)

    print()
    print(f"Rogério e Chaguinha conseguiram encontrar {qtdPos} possíveis posições para as almas se posicionarem sem conflitos!")
    if qtdPos == 0:
        print("Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")
    elif qtdPos <= 10:
        print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")
    elif qtdPos < 50:
        print("Uau! São tantas opções que eles até se perderam contando!")
    else:
        print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")

main()