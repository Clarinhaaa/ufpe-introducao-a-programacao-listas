# formas de potenciação: ** e pow()
# raiz quadrada = potência de 1/2
def calcularDistancia(x1, x2, z1, z2):
    resultado = (((x1 - x2) ** 2) + ((z1 - z2) ** 2)) ** 0.5
    return resultado

xSteve = int(input())
zSteve = int(input())

xVilas = [34, 0, 140]
zVilas = [220, 0, 456]
nomesVilas = ["Hogsmeade", "Kakariko", "Solitude"]

# o for itera os elementos de um array, não contabiliza por um índice geral
# por isso o while, para usar os 3 arrays ao mesmo tempo
i = 0
while (i < len(nomesVilas)):
    distancia = calcularDistancia(xSteve, xVilas[i], zSteve, zVilas[i])
    print(f"Distancia para {nomesVilas[i]}: {round(distancia, 2)}")
    i += 1