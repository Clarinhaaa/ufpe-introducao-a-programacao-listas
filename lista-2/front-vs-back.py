print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")

qtdFrontCampo = 6
qtdFrontMorto = 0
qtdBackCampo = 6
qtdBackMorto = 0

timeAtacante = input()
while timeAtacante != "Front-End" and timeAtacante != "Back-End":
    print("Entrada inválida!")
    timeAtacante = input()

ataque = ""
defesa = ""

while qtdFrontCampo > 0 and qtdBackCampo > 0:
    ataque = input()

    while ataque != "acertou" and ataque != "errou":
        print("Entrada inválida!")
        ataque = input()

    if ataque == "acertou":
        if timeAtacante == "Front-End":
            qtdBackCampo -= 1
            qtdBackMorto += 1
        else:
            qtdFrontCampo -= 1
            qtdFrontMorto += 1
        print(f"{timeAtacante} acertou um jogador!")
        print(f"Back-End: {qtdBackCampo} dev(s) em campo. | Front-End: {qtdFrontCampo} dev(s) em campo.")
        timeAtacante = "Back-End" if timeAtacante == "Front-End" else "Front-End"
    # else: nada acontece, o ataque do morto vai acontecer se acertar e pode não acontecer se errar e passar na
    # verficação dos mortos, então o próximo bloco vai rodar de qualquer jeito

    # verifica se o time da vez, que errou o ataque, está sem mortos
    if ataque == "errou" and ((qtdFrontCampo == 6 and timeAtacante == "Front-End") or (qtdBackCampo == 6 and timeAtacante == "Back-End")):
        timeAtacante = "Back-End" if timeAtacante == "Front-End" else "Front-End"
    else:
        if qtdBackCampo > 0 and qtdFrontCampo > 0:
            # gambiarra para fazer com que, quando o time da vez acerte, o morto do time oposto possa jogar
            defesa = input() if ataque == "errou" else "deixou"

            while defesa != "pegou" and defesa != "deixou":
                print("Entrada inválida!")
                defesa = input()

            if defesa == "pegou":
                timeAtacante = "Back-End" if timeAtacante == "Front-End" else "Front-End"
            else:
                ataque = input() # ataque do morto
                while ataque != "acertou" and ataque != "errou":
                    print("Entrada inválida!")
                    ataque = input()

                while ataque == "acertou":
                    if timeAtacante == "Front-End":
                        qtdFrontMorto -= 1
                        qtdFrontCampo += 1
                        qtdBackMorto += 1
                        qtdBackCampo -= 1
                    else:
                        qtdBackMorto -= 1
                        qtdBackCampo += 1
                        qtdFrontMorto += 1
                        qtdFrontCampo -= 1
                    print(f"O morto do {timeAtacante} acertou um jogador!")
                    print(f"Back-End: {qtdBackCampo} dev(s) em campo. | Front-End: {qtdFrontCampo} dev(s) em campo.")
                    timeAtacante = "Back-End" if timeAtacante == "Front-End" else "Front-End"
                    ataque = input() if qtdFrontCampo > 0 and qtdBackCampo > 0 else "errou"
                
                # defesa do time oposto se o morto errar
                defesa = input() if qtdFrontCampo > 0 and qtdBackCampo > 0 else "deixou"

                while defesa != "pegou" and defesa != "deixou":
                    print("Entrada inválida!")
                    defesa = input()

                if defesa == "pegou":
                    timeAtacante = "Front-End" if timeAtacante == "Back-End" else "Back-End"
                # else: a vez continua sendo da mesma equipe, então o time atacante não muda

if qtdFrontCampo == 0: # Back ganhou
    print(f"Vitória do Back-End! Restaram {qtdBackCampo} devs ainda mantendo o servidor de pé!")
else: # Front ganhou
    print(f"Vitória do Front-End! Restaram {qtdFrontCampo} devs ainda segurando o layout!")