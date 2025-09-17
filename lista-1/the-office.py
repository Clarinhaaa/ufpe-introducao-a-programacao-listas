nomeItem = input().lower()
valorItem = float(input())
nomePessoa = input().lower()
evento = input().lower()

# acima do orçamento
if valorItem > 100:
    if nomePessoa == "angela":
        print("Compra Aprovada!")
        print("Apenas eu tenho discernimento para gastos desta magnitude.")
    else:
        print("Compra Reprovada!")
        print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")
# dentro do orçamento angela
elif nomePessoa == "angela":
    print("Compra Aprovada!")
    print("Compra feita por mim, obviamente dentro dos padrões de excelência.")
# michael
elif nomePessoa == "michael":
    if nomeItem == "mágica" or nomeItem == "fantasia":
        print("Compra Reprovada!")
        print("O Comitê não financia frivolidades e palhaçadas, Michael.")
    elif valorItem > 60:
        print("Compra Aprovada com ressalvas!")
        if evento == "natal":
            print("O espírito natalino de Michael é... excessivo. A nota será conferida.")
        elif evento == "aniversário":
            print("Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
    else:
        print("Compra Aprovada!")
        print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")
# halloween
elif evento == "halloween":
    if nomeItem == "abóbora":
        if valorItem <= 30:
            print("Compra Aprovada!")
            print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
        else:
            print("Compra Aprovada com ressalvas!")
            print("Por que uma abóbora precisa ser tão cara? Extravagância.")
    else:
        print("Compra Aprovada com ressalvas!")
        print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
# aniversário
elif evento == "aniversário":
    if nomeItem == "bolo" and valorItem <= 40:
        print("Compra Aprovada!")
        print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
    elif nomeItem == "sorvete de menta com chocolate":
        print("Compra Reprovada!")
        print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
    else:
        print("Compra Aprovada!")
        print("Itens de aniversário devem ser práticos, não uma distração do trabalho.")
# regras gerais
else:
    if valorItem > 50:
        print("Compra Aprovada com ressalvas!")
        print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")
    else:
        print("Compra Aprovada!")
        print("Esta compra não viola nenhum regulamento... por enquanto.")