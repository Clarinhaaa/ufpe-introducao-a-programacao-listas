nome1 = input()
pas1 = int(input())

nome2 = input()
pas2 = int(input())

nome3 = input()
pas3 = int(input())

if nome1 != "Lineu" and nome2 != "Lineu" and nome3 != "Lineu":
    nomeVencedor = ""
    pasVencedor = -1
    
    if pas1 > pas2 and pas1 > pas3:
        nomeVencedor = nome1
        pasVencedor = pas1
    elif pas2 > pas3:
        nomeVencedor = nome2
        pasVencedor = pas2
    else:
        nomeVencedor = nome3
        pasVencedor = pas3
    print(f"A(O) campeã(o) é {nomeVencedor}, com {pasVencedor} pastéis consumidos!")

    if (nome1 == "Floriano" or nome2 == "Floriano" or nome3 == "Floriano") and nomeVencedor != "Floriano":
        print(f"Anos comendo pastel e perdeu justo para {nomeVencedor}, lastimável, Sr. Flor!")

    if nomeVencedor == "Agostinho":
        if (pasVencedor > 100):
            print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
        elif (pasVencedor < 100 and pasVencedor > 50):
            print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
else:
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")