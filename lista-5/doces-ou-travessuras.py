# função que retorna a quantidade de partições de um número "num"

# parecida com uma função recursiva de combinações, ela verifica as possibilidades de usar um número
# "k" na soma da partição, ou não. "k" seria o maior número disponível para utilizar na contagem de possibilidades

# se usar, será contabilizada a quantidade de possibilidades de partições com as somas que chegam na diferença
# de num - k (por exemplo, num = 6 e k = 4, se usar "k", terei que ver as partições para 2, ou seja: 4, 2 e 4, 1, 1)

# se não usar, k é decrementado em 1 e serão contabilizadas as partições de "num" que não usam o "k" anterior

def contarParticoes(num, k): #* int
    #* casos base para partições encontradas
    # num == 0: todos os "k" necessários para somar "num" foram utilizados
    # num == 1: a única partição de 1 é o próprio 1
    # k == 1: há apenas uma forma de escrever a soma de um número usando 1, que é o 1 repetido "num" vezes
    if num == 0 or num == 1 or k == 1:
        return 1
    #* caso base para partições inválidas
    # num < 0: a soma dos "k" utilizados ultrapassou "num", logo, a partição não existe
    if num < 0:
        return 0
    #* caso recursivo
    # contarParticoes(num - k, k): "usa" o k nas partições
    # contarParticoes(num, k - 1): não "usou" o k anterior nas partições
    return contarParticoes(num - k, k) + contarParticoes(num, k - 1)

def main():
    numDoces = int(input())
    qtdParticoes = contarParticoes(numDoces, numDoces)

    print("DOCES OU TRAVESSURAS???")
    print(f"sem travessuras por hoje! tenho {qtdParticoes} sacolinhas pra vocês")
    if qtdParticoes % 2 == 0:
        print("doces equilibrados, sem travessuras!")
    else:
        print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
    
main()