# essa com certeza não é a forma que o criador da questão imaginou que ela seria respondida kk,
# mas também percebi que, dessa forma, dá certo

# é uma função recursiva que já considera as ferramentas que gastam menos energia a cada hora,
# já que, se o jogador não conseguir sobreviver gastando menos energia possível, não é gastando
# mais que ele vai

# dessa forma, a recursão apenas avança cada hora na noite e retorna a energia restante, juntamente
# às escolhas que foram tomadas ao longo das chamadas, se o jogador sobreviver a noite

# esse retorno se dá através de uma lista com a energia restante e as escolhas de ferramentas, do
# horário mais avançado até a meia-noite

# se o jogador não sobreviver, a função retornará None

def sobreviverHora(horario, energia, difi, ferramentas, goldenF):
    # casos base:
    # não sobreviveu
    if energia <= 0:
        return None
    # sobreviveu
    if horario == 6:
        return [energia]
    
    # resetando as ferramentas para a próxima hora
    # modelo das ferramentas: [PE, PD, LZ, CAM]
    ferramentas = [False, False, False, False]
    # verificação dos horários e ataques
    if horario != 2: # às 2h, ninguém ataca
        if horario == 0 or horario == 3:
            if difi[0] != 0: # Bonnie
                # desliga as luzes
                ferramentas[2] = True
                energia -= (3 + (difi[0] * 0.25))
        elif horario == 1 or horario == 4:
            if horario == 4 and energia > 50 and difi[3] != 0: # Foxy
                # fecha a porta esquerda
                ferramentas[0] = True
                energia -= (5 + (difi[3] * 0.15))
            if difi[1] != 0: # Chica
                # fecha a porta direita
                ferramentas[1] = True
                energia -= (2 + (difi[1] * 0.35))
        else:
            if difi[2] != 0: # Freddy
                # olha as câmeras
                ferramentas[3] = True
                energia -= (3 + (difi[2] * 0.35))
                if goldenF: # Golden Freddy
                    energia -= (10 + (difi[2] * 1.95))

    # desconta a energia das ferramentas
    if ferramentas[0]: energia -= 7
    if ferramentas[1]: energia -= 7
    if ferramentas[2]: energia -= 5
    if ferramentas[3]: energia -= 9

    retorno = sobreviverHora(horario + 1, energia - 1, difi, ferramentas.copy(), goldenF)
    return retorno if retorno == None else retorno + [ferramentas]

def converterLista(lista):
    lista = [int(num) for num in lista]
    return lista

def validarInput(difi):
    difi = converterLista(difi)
    if len(difi) == 4:
        for num in difi:
            if num < 0 or num > 20:
                return False
        return True
    return False

def main():
    # modelo das dificuldades: [Bonnie, Chica, Freddy, Foxy]
    dificuldades = input().split(" ")

    if not validarInput(dificuldades):
        print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')
    elif dificuldades == ["0", "0", "0", "0"]:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    else:
        # pegando todos os algarismos das dificuldades, para verificar se há os números de 1987
        # juntamente com o 0
        dificuldadesAux = []
        for num in dificuldades:
            dificuldadesAux += ([char for char in list(num)])

        goldenF = False
        mensagemGolden = ""

        # verificando o anagrama de 1987
        if "1" in dificuldadesAux and "9" in dificuldadesAux and "8" in dificuldadesAux and "7" in dificuldadesAux:
            goldenF = True
            if "0" in dificuldadesAux:
                mensagemGolden = "IT'S ME"
                print(f'"{mensagemGolden}"')

        # se o Golden Freddy não entrou no caso especial, o programa roda normalmente, mesmo com o anagrama
        if mensagemGolden == "":
            dificuldades = converterLista(dificuldades)
            melhoresEscolhas = sobreviverHora(0, 100.0, dificuldades, [False, False, False, False], goldenF)
            if melhoresEscolhas == None:
                print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')
            else:
                melhoresEscolhas.reverse()
                energia = melhoresEscolhas.pop()
                print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia:.2f}% de energia. Eu sabia que você conseguiria."')
                for i in range(6):
                    print(f'0{i}:00 AM -> PE: {"SIM" if melhoresEscolhas[i][0] else "NÃO"} | PD: {"SIM" if melhoresEscolhas[i][1] else "NÃO"} | LZ: {"SIM" if melhoresEscolhas[i][2] else "NÃO"} | CAM: {"SIM" if melhoresEscolhas[i][3] else "NÃO"}')

main()