# a recursão desta função ocorre na hora de obter o índice da letra chave, que serve para
# descobrir o índice da próxima chave para a próxima letra e assim por diante

# dessa forma, o parâmetro idxAtual representa o índice da letra que está sendo descriptografada na string da mensagem
# e ele será decrementado a cada chamada recursiva, pois o parâmetro letraAtual recebe o retorno de textoCripto.pop()
# então esse código começa a analisar cada letra da mensagem no retorno da recursão, começando pela primeira

def descriptografar(textoCripto, letraChave, idxAtual, letraAtual="(●'◡'●)"): # Chara jumpscare
    # caso base: quando a string da mensagem criptografada estiver vazia
    if idxAtual < 0:
        return letraChave, []
    
    # adicionando o kaomoji à lista para caso a letraAtual ainda não esteja definida
    # créditos a Lucas Oliveira de EC por ter me inspirado a usar uma string diferentona pra lidar com armadilhas
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z", "(●'◡'●)"]


    # atualizando a letra atual para a próxima chamada
    letraAtual = textoCripto.pop() if (len(textoCripto) - 1) >= 0 else "(●'◡'●)"

    # obtendo o índice no alfabeto da letra atual da mensagem criptografada
    if letraAtual in alfabeto: idxLetraCripto = alfabeto.index(letraAtual)

    # caso recursivo:
    # pegando a letra chave da vez, pegando a útima letra da mensagem descriptografada e a lista de armadilhas
    # que pode ter sido atualizada
    textoDecripto, listaArmadilhas = descriptografar(textoCripto, letraChave, idxAtual - 1, letraAtual)

    # caso da armadilha: a lista de índices das armadilhas é atualizada
    # decremento mais uma vez o idxAtual, para "pular" o caractere inválido
    # atualizo tanto letraAtual como textoCripto, para também "pular" o caractere invállido
    if letraAtual not in alfabeto:
        listaArmadilhas.append(str(idxAtual))
        textoDecripto += ""
    else:
        letraChave = textoDecripto[-1]
        # obtendo o índice da letra chave no alfabeto
        idxLetraChave = alfabeto.index(letraChave)
        
        idxLetraDecripto = (idxLetraCripto - idxLetraChave) % 26
        # atualizando a mensagem descriptografada
        textoDecripto += alfabeto[idxLetraDecripto]

    return textoDecripto, listaArmadilhas
    
def main():
    chaveInicial = input()
    textoCripto = list(input())

    print("Decifrando mensagem do Trickster...")
    # idxAtual começa como o último índice de textoCripto
    textoDecripto, listaArmdadilhas = descriptografar(textoCripto, chaveInicial, len(textoCripto) - 1)
    
    if len(listaArmdadilhas) > 0:
        print(f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {', '.join(listaArmdadilhas)}")
    else:
        print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")
    print(f"Mensagem revelada: {textoDecripto[1:]}")
    # a função ficou colocando a chave inicial na mensagem descriptografada, então eu imprimo a partir do index 1
    
main()