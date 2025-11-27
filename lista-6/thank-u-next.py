def verificarCategoria(dici, categoria): # retorna uma tupla vazia caso a categoria não exista
    tuplaItem = dici.get(categoria)
    return tuplaItem if type(tuplaItem) is tuple else () # se a categoria não existe, get() retorna o tipo NoneType

def main():
    strInput = ""
    exigenciasAri = {}
    qtdDividasPendentes = 0
    # variáveis de controle usadas ao longo do código:
    # strInput - string usada para verificação do input nos blocos while
    # listaInput - usada para tratar as informações importantes das strInput e armazená-las em seus devidos lugares
    # qtdItemAtual - representa a quantidade de cada item exigido, presente nas tuplas

    # FASE 1: exigências de Ariana
    # preenchendo o dicionário com os itens da dívida
    while strInput != "MIMOS RECEBIDOS":
        strInput = input()
        if strInput != "MIMOS RECEBIDOS":
            listaInput = strInput.split(": ")
            qtdItemAtual = int(listaInput[2])
            # incrementando o latte extra na dívida
            if listaInput[0] == "Bebidas" and listaInput[1] == "latte":
                qtdItemAtual += 1
            # formando o dicionário
            exigenciasAri[listaInput[0]] = (listaInput[1], qtdItemAtual)
    
    # FASE 2: reabastecimento
    while strInput != "ACABOU, a Glinda está pronta!":
        strInput = input()
        if strInput != "ACABOU, a Glinda está pronta!":
            listaInput = strInput.split(" ")

            qtdItemChegou = int(listaInput[1])
            keyItem = listaInput[5] # armazenando a categoria que chegou

            tuplaItem = verificarCategoria(exigenciasAri, keyItem)
            # atualizando a quantidade do item no dicionário
            if len(tuplaItem) > 0:
                qtdItemAtual = tuplaItem[1] - qtdItemChegou
                exigenciasAri.update({keyItem: (tuplaItem[0], qtdItemAtual)})

    # RELATÓRIO FINAL
    print('Relatório de Balanço Final:')
    fraseDivida = ""

    for k, v in exigenciasAri.items():
        if v[1] <= 0:
            fraseDivida = "Você entregou TUDO! O mimo tá mais que garantido."
        else:
            fraseDivida = f"Golpe BAIXÍSSIMO! Faltam {v[1]} mimos. Corre!"
            qtdDividasPendentes += 1 # atualizando as dívidas não alcançadas

        print(f'Categoria: {k} Item: {v[0]} Status: {fraseDivida}')
    print()

    # verificando caso especial de Maquiagem-gloss
    tuplaItem = verificarCategoria(exigenciasAri, "Maquiagem")
    if len(tuplaItem) > 0 and tuplaItem[0] == "Gloss":
        if tuplaItem[1] <= 0:
            print('TUDO! O Gloss tá on. O look de Glinda tá salvo!') 
        else:
            print('CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!')
    # verificando caso especial de Bebidas-latte
    tuplaItem = verificarCategoria(exigenciasAri, "Bebidas")
    if len(tuplaItem) > 0 and tuplaItem[0] == "latte":
        if tuplaItem[1] <= 0:
            print('Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take')
        else:
            print('Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!')
    print()

    # COMENTÁRIO FINAL DE ARIANA
    print('Veredito Final')
    if qtdDividasPendentes >= 3:
        print('Thank U, Next! A equipe de camarim foi demitida!')
    else:
        print('Estoque Aprovado! Glinda vai brilhar em Wicked!')

main()