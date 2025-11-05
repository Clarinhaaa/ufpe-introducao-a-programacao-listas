def acaoGreatSword(acao): #* int
    if acao == "Golpe Carregado":
        return 165
    elif acao == "Corte Largo":
        return 120
    else: # "Divisor de Mundos"
        return 200

def acaoGlaiveInseto(acao): #* int
    if acao == "Corte Aéreo":
        return 100
    elif acao == "Descida Carregada":
        return 120
    else: # "Kinseto"
        corExtrato = input()
        if corExtrato == "Vermelho":
            return 40
        elif corExtrato == "Amarelo":
            return 15
        else: # "Verde"
            return 0
        
def acaoFuziArco(acao): #* int
    if acao == "Tiro Carregado":
        return 90
    elif acao == "Bala de Penetração":
        return 120
    else: # "Tiro Devastador"
        return 150

def acaoFatalis(acao, vidaCacadores): #* list[int]
    statusCacadores = ["Desprotegido", "Desprotegido", "Desprotegido"]

    if acao == "Ataque com Cauda":
        for i in range(3):
            vidaCacadores[i] -= 55
    elif acao == "Bola de Fogo":
        for i in range(3):
            vidaCacadores[i] -= 65
    else: # "Mar de Chamas Negras"
        for i in range(3):
            if vidaCacadores[i] > 0:
                statusCacadores[i] = input()
                if statusCacadores[i] == "Desprotegido":
                    vidaCacadores[i] = 0
    
    return vidaCacadores

def main():
    print("Hora de Lutar contra a Historia!")
    print()

    vidaFatalis = 1800
    # cacadores[0] = greatSword, caçadores[1] = glaiveInseto, caçadores[2] = fuziArco
    vidaCacadores = [200, 200, 200]
    
    for i in range(4):
        # O(s) caçador(es) vivo(s) realizam suas ações
        if vidaCacadores[0] > 0: vidaFatalis -= acaoGreatSword(input())
        if vidaCacadores[1] > 0:
            resultadoGlaive = acaoGlaiveInseto(input())
            if resultadoGlaive != 0: vidaFatalis -= resultadoGlaive
            else: vidaCacadores[1] += 40
        if vidaCacadores[2] > 0: vidaFatalis -= acaoFuziArco(input())

        # Fatalis vai agir SE tiver pelo menos 1 caçador vivo E ele estiver vivo
        if (vidaCacadores[0] > 0 or vidaCacadores[1] > 0 or vidaCacadores[2] > 0) and vidaFatalis > 0:
            vidaCacadores = acaoFatalis(input(), vidaCacadores)

    if vidaFatalis <= 0:
        print("Eu não acredito, vocês conseguiram!\nObrigado caçadores! O mundo está salvo.")
    else: # vidaCacadores == [0, 0, 0]
        print("O Fatalis conseguiu sobreviver ao combate...\nO mundo corre perigo!")

main()