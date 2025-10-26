print("Senhoras e senhores, o desfile de gala do CIn vai começar!")

qtdPessoas = int(input())
marcaPatrociandor = input()
nomePatrocinador = ""
if marcaPatrociandor == "Tha Beauty":
    nomePatrocinador = "Thais Linares"
elif marcaPatrociandor == "DeGuê?":
    nomePatrocinador = "Davi Brito"
else:
    nomePatrocinador = "Edu e Fih"

listMonitores = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
listMonitoresDisponiveis = listMonitores.copy()
listDesfilantes = []
listIntrusos = []

qtdInvasoes = 0
invadiu = False

for i in range(qtdPessoas):
    listDesfilantes.append(input())
    if listDesfilantes[i] in listMonitores:
        listMonitoresDisponiveis.remove(listDesfilantes[i])

for pessoa in listDesfilantes:
    if qtdInvasoes == 3 and "Core" not in listDesfilantes:
        print("Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")
        listDesfilantes.insert(listDesfilantes.index(pessoa), "Core")
        pessoa = "Core"

    if pessoa not in listMonitores and pessoa != "Core":
        if pessoa == nomePatrocinador:
            print("Invasão tolerada por motivos de patrocínio!")
        else:
            print(f"{pessoa} invadiu a passarela! Segurem ele(a), produção!")
            qtdInvasoes += 1
            listIntrusos.append(pessoa)
            if len(listMonitoresDisponiveis) > 0:
                listDesfilantes[listDesfilantes.index(pessoa)] = listMonitoresDisponiveis[0]
                pessoa = listMonitoresDisponiveis[0]
                listMonitoresDisponiveis.remove(pessoa)
            else:
                invadiu = True
    
    if invadiu:
        print(f"Desfilante de n° {listDesfilantes.index(pessoa) + 1}: {pessoa}?! Pelo visto não havia como substituir...")
    else:
        print(f"Desfilante de n° {listDesfilantes.index(pessoa) + 1}: {pessoa}!")

    invadiu = False

if "Gretchen" in listIntrusos or "Tulla Luana" in listIntrusos or "Inês Brasil" in listIntrusos:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")
    for intruso in listIntrusos:
        if intruso == "Gretchen":
            print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
        elif intruso == "Tulla Luana":
            print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')
        elif intruso == "Inês Brasil":
            print('"É aquele ditado... Vamo fazer o quê?"')