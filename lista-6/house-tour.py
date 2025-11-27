def main():
    print('Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?')
    print('A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…')
    print()

    catalogoPhil = {}
    listaInput = []

    qtdCasas = int(input())

    # cadastramento das casas no dicionário catalogoPhil
    # modelo do input das casas: [bairro, endereco, quartos-preco]
    for i in range(qtdCasas):
        listaInput = input().split(" - ")
        catalogoPhil[listaInput[1]] = {
            "bairro": listaInput[0],
            "quartos": int(listaInput[2][0]),
            "preco": int(listaInput[2][2:])}
    listaInput = []

    print('Catálogo concluído! Quem será que irá comprar uma casa de Phil?')
    print()
        
    # cadastramento das clientes
    nomeCliente = ""
    reqCliente = ()
    qtdVendas = 0

    while nomeCliente != "FIM":
        nomeCliente = input()
        if nomeCliente != "FIM":
            # modelo requisitos = (quartosMin, orcamentoMax)
            reqCliente = tuple(input().split("-"))

            # analisando casas válidas para a cliente da vez
            keyMelhorCasa = ""
            maiorScore = 0
            for k in catalogoPhil.keys():
                if catalogoPhil[k]["quartos"] >= int(reqCliente[0]) and catalogoPhil[k]["preco"] <= int(reqCliente[1]):
                    # se a casa é válida, calcula o score e decide qual é a melhor casa
                    scoreAtual = catalogoPhil[k]["quartos"] * 10

                    if scoreAtual > maiorScore:
                        keyMelhorCasa = k
                        maiorScore = scoreAtual
            
            # outputs de casa encontrada ou não
            if keyMelhorCasa == "":
                print(f'Puxa, {nomeCliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.')
                print()
            else:
                print(f'🎤 Bem-vindo ao House Tour de {catalogoPhil[keyMelhorCasa]["bairro"]}, {nomeCliente}!')
                print(f'➡ Casa: {keyMelhorCasa}')
                print(f'💖 Score: {maiorScore} pontos')
                print()

                # reação da cliente
                if maiorScore >= 40: # gostou
                    if nomeCliente == "Sabrina Carpenter":
                        print('"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"')
                    elif nomeCliente == "Taylor Swift":
                        print('"Essa casa é perfeita para passar as férias na praia!"')
                    else:
                        print(f'"{nomeCliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"')
                    print()
                    print('Venda concluída! Phil dança triunfante ao som de "House Tour"!')
                    qtdVendas += 1
                else: # não gostou
                    if nomeCliente == "Sabrina Carpenter":
                        print('"Hmm... Sabe Phil, a letra não era tão literal assim…"')
                    elif nomeCliente == "Taylor Swift":
                        print('"Nós nunca vamos comprar essa casa juntos, Phil!"')
                    else:
                        print('"Parece que a música não ajudou nas vendas dessa vez…"')
                    print()
                    print('Talvez a Sabrina realmente não estivesse falando de imóveis…')
                print()

    print('===== RELATÓRIO DE VENDAS =====')
    print(f'Total de casas vendidas: {qtdVendas}')
    print('===============================')

main()