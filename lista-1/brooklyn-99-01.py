casos = int(input())
dias = int(input())

mediaDiaria = casos / dias

assistencias = int(input())
operCampo = int(input())

isOperEspecial = input().lower()
if isOperEspecial == "sim":
    tipoOperEspecial = input().lower()

localizacao = input().lower()

pontuacao = -1

if localizacao == "manhattan" or localizacao == "brooklyn":
    print("Pelo menos nos bairros corretos Jake está!")
    if casos >= 20:
        print("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
        pontuacao += casos * 2
        if mediaDiaria >= 0.5:
            print("Parece que Jake é bem consistente na sua média diária de casos.")
            if assistencias >= 5:
                print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")
                pontuacao += assistencias * 1.5
                if operCampo >= 20:
                    print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
                    pontuacao += operCampo * 0.5
                    if isOperEspecial == "sim":
                        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
                        if tipoOperEspecial == "infiltração":
                            pontuacao /= 0.5
                        elif tipoOperEspecial == "escuta":
                            pontuacao /= 0.3
                        elif tipoOperEspecial == "invasão":
                            pontuacao /= 0.2
                        else:
                            pontuacao /= 0.1
                    else:
                        print("Para que operação especial quando se tem números, não é?")
                    # resultados
                    if pontuacao >= 70:
                        print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
                    elif pontuacao < 70 and pontuacao >= 40:
                        print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
                    else:
                        print("Muito difícil de Jake ganhar o prêmio.")
                else:
                    print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")
            else:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")
        else:
            print("A média diária de casos tá muito baixa, Peralta foi desclassificado.")
    else:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
else:
    print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")