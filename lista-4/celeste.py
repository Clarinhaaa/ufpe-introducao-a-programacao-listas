# Ambas as funções de ataque e reação imprimem o devido output
# e retornam o novo valor calulado da vida de Madeline

def ataqueBadeline(ataque, vida):
    if ataque == "Você não tem o que é necessário para escalar.":
        print("Eu nunca vou conseguir chegar ao topo :(")
        vida -= 20
    else: # "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!"
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
        vida -= 50

    return vida

def reacaoMadeline(reacao, vida):
    qtdRespiracoes = 0

    if reacao == "Calma Badeline, nós vamos conseguir.":
        vida += 25
    elif reacao == "Eu sei que somos capazes! Vamos em frente!":
        qtdRespiracoes = int(input())
        vida += (10 * qtdRespiracoes)
    else: # "Madeline, nós estamos com você. Continue!"
        vida += 60
        
    return vida

def main():
    vidaMadeline = 100
    fraseInput = ""

    while vidaMadeline > 0 and vidaMadeline < 150:
        fraseInput = input()
        vidaMadeline = ataqueBadeline(fraseInput, vidaMadeline)

        if vidaMadeline > 0:
            fraseInput = input()
            vidaMadeline = reacaoMadeline(fraseInput, vidaMadeline)

    if vidaMadeline >= 150:
        print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")
    else:
        print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")

main()