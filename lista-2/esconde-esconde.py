pessoa1 = input()
pessoa2 = input()
pessoa3 = input()

ptsPessoa1 = 0
ptsPessoa2 = 0
ptsPessoa3 = 0

siglaPredio = ""
textoBusca = ""
fimBusca = False

print("Vai começar o esconde-esconde UFPE 2025!")

print(f"\nProntos ou não, lá vai {pessoa1}.")

for i in range(3):
    fimBusca = False

    siglaPredio = "CFCH" if i == 0 else "CTG" if i == 1 else "CIN"
    print(f"Agora {pessoa1} procurará no {siglaPredio}.")
    while not fimBusca:
        textoBusca = input()
        if textoBusca == "Achou uma pessoa!": 
            ptsPessoa1 += 1
            print(f"{pessoa1} achou uma pessoa!")
        else: fimBusca = True

print(f"\nProntos ou não, lá vai {pessoa2}.")

for i in range(3):
    fimBusca = False
    
    siglaPredio = "CFCH" if i == 0 else "CTG" if i == 1 else "CIN"
    print(f"Agora {pessoa2} procurará no {siglaPredio}.")
    while not fimBusca:
        textoBusca = input()
        if textoBusca == "Achou uma pessoa!": 
            ptsPessoa2 += 1
            print(f"{pessoa2} achou uma pessoa!")
        else: fimBusca = True

print(f"\nProntos ou não, lá vai {pessoa3}.")

for i in range(3):
    fimBusca = False

    siglaPredio = "CFCH" if i == 0 else "CTG" if i == 1 else "CIN"
    print(f"Agora {pessoa3} procurará no {siglaPredio}.")
    while not fimBusca:
        textoBusca = input()
        if textoBusca == "Achou uma pessoa!": 
            ptsPessoa3 += 1
            print(f"{pessoa3} achou uma pessoa!")
        else: fimBusca = True

if ptsPessoa1 == 0 and ptsPessoa2 == 0 and ptsPessoa3 == 0:
    print("\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
else:
    if ptsPessoa1 > ptsPessoa2 and ptsPessoa1 > ptsPessoa3:
        print(f"\n{pessoa1} é o(a) melhor no esconde-esconde da UFPE!")
    elif ptsPessoa2 > ptsPessoa3:
        print(f"\n{pessoa2} é o(a) melhor no esconde-esconde da UFPE!")
    else:
        print(f"\n{pessoa3} é o(a) melhor no esconde-esconde da UFPE!")