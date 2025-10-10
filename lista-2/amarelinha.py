jogadores = "aAJD" # ana, Adrieli, Joab, Duda

tentPorJogador = int(input())
tentDaRodada = 0 # segundo input, as últimas casas do jogador para aquela rodada
completou = False

# quantidade de pessoas que chegaram na casa 5, frase para 1 vencedor e string com os vencedores empatados
qtdVencedores = 0
fraseUmVencedor = "O vencedor é "
empatados = ""
primeiroNome = True

for i in jogadores:
    completou = False

    for j in range(tentPorJogador):
        tentDaRodada = int(input())
        if tentDaRodada == 5:
            completou = True
        
    if tentDaRodada == 5: qtdVencedores += 1

    # atribuição das últimas tentativas de cada jogador
    if i == "a":
        print(f"Ana tentou {tentPorJogador} vezes e completou a última casa {tentDaRodada}")
        # se Ana chegou ao final ou não
        if completou: 
            fraseUmVencedor += "Ana!"
            if not primeiroNome: empatados += ", "
            empatados += "Ana"
            primeiroNome = False
            print("Ana completou a amarelinha!")
        else: print("Ana não conseguiu completar a amarelinha!")
    elif i == "A":
        print(f"Adrieli tentou {tentPorJogador} vezes e completou a última casa {tentDaRodada}")
        # se Adrieli chegou ao final ou não
        if completou: 
            fraseUmVencedor += "Adrieli!"
            if not primeiroNome: empatados += ", "
            empatados += "Adrieli"
            primeiroNome = False
            print("Adrieli completou a amarelinha!")
        else: print("Adrieli não conseguiu completar a amarelinha!")
    elif i == "J":
        print(f"Joab tentou {tentPorJogador} vezes e completou a última casa {tentDaRodada}")
        # se Joab chegou ao final ou não
        if completou: 
            fraseUmVencedor += "Joab!"
            if not primeiroNome: empatados += ", "
            empatados += "Joab"
            primeiroNome = False
            print("Joab completou a amarelinha!")
        else: print("Joab não conseguiu completar a amarelinha!")
    else:
        print(f"Duda tentou {tentPorJogador} vezes e completou a última casa {tentDaRodada}")
        # se Duda chegou ao final ou não
        if completou: 
            fraseUmVencedor += "Duda!"
            if not primeiroNome: empatados += ", "
            empatados += "Duda"
            primeiroNome = False
            print("Duda completou a amarelinha!")
        else: print("Duda não conseguiu completar a amarelinha!")

    # gostaria de pedir perdão pela gambiarra pro texto dos empatados kkkkkk, saudades vetorzinho

if qtdVencedores == 1:
    print(fraseUmVencedor)
else:
    print(f"Houve empate entre: {empatados}")