# INPUT
participante01 = input().lower()
participante02 = input().lower()
participante03 = input().lower()
participante04 = input().lower()

# competição cancelada
if "terry" in f"{participante01} {participante02} {participante03} {participante04}" or "holt" in f"{participante01} {participante02} {participante03} {participante04}":
    print("Bem-vindos ao Jimmy Jab!")
    print("Jimmy Jab CANCELADO!")

# competição NÃO cancelada
# bocatona
else:
    if "scully" in f"{participante01} {participante02} {participante03} {participante04}":
        vencedorBocatona = "scully"
    else:
        vencedorBocatona = input().lower()

    perdedorBocatona = input().lower()

    participante11 = participante01 if perdedorBocatona != participante01 else participante02
    participante12 = participante02 if perdedorBocatona != participante02 else participante03
    participante13 = participante03 if perdedorBocatona != participante03 else participante04

    # corrida volumosa
    tempo1 = int(input())
    tempo2 = int(input())
    tempo3 = int(input())
    vencedorCorrida = ""
    perdedorCorrida = ""

    if tempo1 < tempo2 and tempo1 < tempo3:
        vencedorCorrida = participante11
    elif tempo2 < tempo3:
        vencedorCorrida = participante12
    else:
        vencedorCorrida = participante13

    if tempo1 > tempo2 and tempo1 > tempo3:
        perdedorCorrida = participante11
    elif tempo2 > tempo3:
        perdedorCorrida = participante12
    else:
        perdedorCorrida = participante13

    # final
    finalista1 = participante11 if perdedorCorrida != participante11 else participante12
    finalista2 = participante12 if perdedorCorrida != participante12 else participante13

    if (finalista1 == "jake" or finalista2 == "jake") and (finalista1 == "amy" or finalista2 == "amy"):
        segundoLugar = "jake"
        primeiroLugar = "amy"
    else:
        primeiroLugar = input().lower()
        segundoLugar = finalista1 if primeiroLugar != finalista1 else finalista2

    # OUTPUT
    print("Bem-vindos ao Jimmy Jab!")

    # bocatona
    print("Nosso primeiro evento é...\nA Bocatona!")
    if vencedorBocatona == "scully":
        print("Scully leva a melhor, não tem como competir com ele.")
    else:
        print(f"{vencedorBocatona.capitalize()} levou a melhor na Bocatona!")
    print(f"{perdedorBocatona.capitalize()} não avançou para a próxima fase!")

    # corrida volumosa
    print("O segundo evento é A corrida volumosa!")
    print(f"{vencedorCorrida.capitalize()} levou a melhor na Corrida Volumosa!")
    print(f"{perdedorCorrida.capitalize()} não avançou para a próxima fase!")

    # final
    print(f"{segundoLugar.capitalize()} ficou com o 2º lugar!\n{primeiroLugar.capitalize()} VENCEU O JIMMY JABS!")