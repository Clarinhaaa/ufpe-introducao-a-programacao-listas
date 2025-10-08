qtdDoces = int(input())
qtdRodadas = qtdDoces // 10

isDivisivel10 = qtdDoces % 10 == 0
if not isDivisivel10: qtdRodadas += 1

jogador1 = input()
jogador2 = input()
vidaJogador1 = 10
vidaJogador2 = 10
jogada1 = ""
jogada2 = ""

vencedorRodada = ""

if "Arthur" not in f"{jogador1} {jogador2}":
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")

    for i in range(qtdRodadas):
        vidaJogador1 = 10
        vidaJogador2 = 10

        if i == 0 and not isDivisivel10: print(f"Pra aquecer, essa primeira vale menos, só {qtdDoces % 10} doces!")
        else: print(f"Batalha número {i + 1}!")

        while vidaJogador1 > 0 and vidaJogador2 > 0:
            jogada1 = input()
            jogada2 = input()

            if jogada1 == jogada2: print("Eita, jogaram a mesma coisa dessa vez.")
            else:
                if jogada1 == "papel":
                    if jogada2 == "tesoura":
                        vidaJogador1 -= 3
                        vidaJogador2 += 1
                    else: # pedra
                        vidaJogador1 += 2
                        vidaJogador2 -= 2
                elif jogada1 == "pedra":
                    if jogada2 == "papel":
                        vidaJogador1 -= 2
                        vidaJogador2 += 2
                    else: # tesoura
                        vidaJogador2 -= 4
                else: # tesoura
                    if jogada2 == "pedra":
                        vidaJogador1 -= 4
                    else: # papel
                        vidaJogador1 += 1
                        vidaJogador2 -= 3
                
                if vidaJogador1 < 0: vidaJogador1 = 0
                if vidaJogador2 < 0: vidaJogador2 = 0

                print(f"Esse turno terminou com {jogador1} tendo {vidaJogador1} de vida e {jogador2} tendo {vidaJogador2}!")

        vencedorRodada = jogador1 if vidaJogador2 == 0 else jogador2
        print(f"A rodada {i + 1} vai para {vencedorRodada}, que garante seus doces!")