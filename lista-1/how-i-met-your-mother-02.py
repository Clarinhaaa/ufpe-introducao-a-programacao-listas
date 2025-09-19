qtdPessoas = int(input())

nome1, nome2, nome3, nome4 = ".", ".", ".", "."
fraseNome1, fraseNome2, fraseNome3, fraseNome4 = "", "", "", ""

if qtdPessoas > 0:
    nome1 = input()
    if nome1 == "Barney":
        fraseNome1 = "Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO."
    elif nome1 == "Robin":
        fraseNome1 = "Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda."
    elif nome1 == "Marshall":
        fraseNome1 = "O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade."
    elif nome1 == "Lily":
        fraseNome1 = "Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”."
    else:
        fraseNome1 = f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera."
    if qtdPessoas > 1:
        nome2 = input()
        if nome2 == "Barney":
            fraseNome2 = "Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO."
        elif nome2 == "Robin":
            fraseNome2 = "Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda."
        elif nome2 == "Marshall":
            fraseNome2 = "O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade."
        elif nome2 == "Lily":
            fraseNome2 = "Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”."
        else:
            fraseNome2 = f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera."
        if qtdPessoas > 2:
            nome3 = input()
            if nome3 == "Barney":
                fraseNome3 = "Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO."
            elif nome3 == "Robin":
                fraseNome3 = "Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda."
            elif nome3 == "Marshall":
                fraseNome3 = "O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade."
            elif nome3 == "Lily":
                fraseNome3 = "Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”."
            else:
                fraseNome3 = f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera."
            if qtdPessoas > 3:
                nome4 = input()
                if nome4 == "Barney":
                    fraseNome4 = "Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO."
                elif nome4 == "Robin":
                    fraseNome4 = "Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda."
                elif nome4 == "Marshall":
                    fraseNome4 = "O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade."
                elif nome4 == "Lily":
                    fraseNome4 = "Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”."
                else:
                    fraseNome4 = f"{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera."
    lugar = input()
else:
    lugar = "MacLaren’s Pub"

if lugar == "MacLaren’s Pub":
    mediaCervejas = int(input())
    qtdCervejas = mediaCervejas * (qtdPessoas + 1)

listaNomes = f"{nome1} {nome2} {nome3} {nome4}"
isQuinteto = "Barney" in listaNomes and "Robin" in listaNomes and "Marshall" in listaNomes and "Lily" in listaNomes

print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

if qtdPessoas > 0:
    print("Hora da lista dos amigos da vez!")

    # verificação de cada nome
    print(fraseNome1)
    if qtdPessoas > 1:
        print(fraseNome2)
        if qtdPessoas > 2:
            print(fraseNome3)
            if qtdPessoas > 3:
                print(fraseNome4)

    # casos específicos de nomes
    if qtdPessoas == 2:
        if nome1 == "Marshall" or nome2 == "Marshall":
            if nome1 == "Lily" or nome2 == "Lily":
                print("Nada melhor que um casal para dar conselhos de relacionamento.")
            elif nome1 == "Barney" or nome2 == "Barney":
                print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    elif qtdPessoas == 4 and isQuinteto:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    # casos específicos de lugares
    if "Barney" in listaNomes and lugar == "Arena de Laser Tag":
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")

    if qtdPessoas == 1 and nome1 == "Robin" and lugar == "Carmichael’s":
        print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")

    if qtdPessoas > 0 and lugar == "MacLaren’s Pub":
        if "Barney" in listaNomes or "Robin" in listaNomes or "Marshall" in listaNomes or "Lily" in listaNomes:
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        else:
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

    # casos de quantidade de pessoas
    fraseQtdPessoas = ""
    pessoas = ""

    if qtdPessoas == 1:
        fraseQtdPessoas = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
        pessoas = nome1
    elif qtdPessoas == 2:
        fraseQtdPessoas = "Duas pessoas se compadeceram com a situação do pobre Ted."
        pessoas = f"{nome1} e {nome2}"
    elif qtdPessoas == 3:
        fraseQtdPessoas = "Três pessoas! Ted conseguiu se divertir bastante."
        pessoas = f"{nome1}, {nome2} e {nome3}"
    elif qtdPessoas == 4:
        if isQuinteto:
            fraseQtdPessoas = "O quinteto junto consegue resolver qualquer problema!"
        else:
            fraseQtdPessoas = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."
        pessoas = f"{nome1}, {nome2}, {nome3} e {nome4}"

    # relatório
    print()
    print("Relatório da situação de Ted:")
    print(f"- Ted foi consolado por: {pessoas}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- {fraseQtdPessoas}")
    if lugar == "MacLaren’s Pub":
        print(f"- Quantidade de cervejas bebidas pelo grupo: {qtdCervejas} cervejas.")
    print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")
    
else:
    # relatório ted sozinho
    print()
    print("Relatório da situação de Ted:")
    print("Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {qtdCervejas} cervejas.")