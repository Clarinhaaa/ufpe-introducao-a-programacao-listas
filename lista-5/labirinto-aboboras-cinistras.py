# calcula os espaços em que Byte pode caminhar antes das chamdas recursivas
def espacosLivres(matriz, iByte, jByte):
    listaEspLivres = []
    espProibidos = ["A", "B"]

    # em cima
    if iByte - 1 >= 0 and matriz[iByte - 1][jByte] not in espProibidos:
        listaEspLivres.append([iByte - 1, jByte])
    
    # embaixo
    if iByte + 1 < len(matriz) and matriz[iByte + 1][jByte] not in espProibidos:
        listaEspLivres.append([iByte + 1, jByte])

    # à esquerda
    if jByte - 1 >= 0 and matriz[iByte][jByte - 1] not in espProibidos:
        listaEspLivres.append([iByte, jByte - 1])

    # à direita
    if jByte + 1 < len(matriz) and matriz[iByte][jByte + 1] not in espProibidos:
        listaEspLivres.append([iByte, jByte + 1])

    return listaEspLivres

# retorna uma string (converter pra list depois) com os minutos restantes de todas as possibilidades de encontrar a saída
# caso ela não seja encontrada em dos caminhos que Byte fizer, nada será adicionado a ela ("")
def vamosByte(matriz, i, j, minRestantes):
    # casos base
    # 1. o tempo acabou
    if minRestantes < 0:
        return ""
    # 2. encontrou a saída
    if matriz[i][j] == "S":
        return f"{minRestantes},"
    
    # caso recursivo
    caminhosPossiveis = "" # string que será retornada
    # marcando os espaços que Byte passou como "B" também, para evitar que passe no lugar de onde veio
    matriz[i][j] = "B"
    listaEspLivres = espacosLivres(matriz, i, j) # vendo se há espaços livres ao redor dele (de forma perpendicular)
    # se listaEspLivres estiver vazia, Byte está em um beco sem saída, então não terá mais caminhos possíveis ("")
    if len(listaEspLivres) > 0:
        # itera por todos os espaços livres em volta de Byte, testando todos os caminhos possíveis do labirinto
        for coordLivre in listaEspLivres:
            caminhosPossiveis += vamosByte(matriz, coordLivre[0], coordLivre[1], minRestantes - 1)
    matriz[i][j] = "0"
    
    return caminhosPossiveis

def main():
    # tratando o input dos minutos restantes
    horas = input().split(":")
    minAtual = int(horas[1])
    minRestantes = 60 - minAtual

    print(f"O relógio marca 23 horas e {minAtual} minuto(s)! Byte tem apenas {minRestantes} minuto(s) para escapar!")

    # criando a matriz do labirinto
    tamanhoLab = int(input())
    labirinto = []
    for i in range(tamanhoLab):
        labirinto.append(list(input()))
        # obtendo as coordenadas de Byte
        if "B" in labirinto[i]:
            iByte = i
            jByte = labirinto[i].index("B")

    caminhosPossiveis = vamosByte(labirinto, iByte, jByte, minRestantes).split(",")
    caminhosPossiveis.pop() # removendo o último caractere vazio que surge após o split()

    if len(caminhosPossiveis) == 0:
        print("NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!")
    else:
        caminhosPossiveis = [int(cam) for cam in caminhosPossiveis] # convertendo a lista de str para int
        minFolga = max(caminhosPossiveis) # obtendo os minutos de folga da possibilidade de caminho mais curto
        
        print(f"CONSEGUIMOS!! Byte precisou de {minRestantes - minFolga} minuto(s) para conseguir escapar!")
        if minFolga > 10:
            print(f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {minFolga} minutos para elas acordarem")
        else:
            print("Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.")

main()