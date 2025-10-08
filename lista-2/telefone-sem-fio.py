qtdJogadores = int(input())

print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")

nome = input()
nomeErro1, nomeErro2 = "", ""

primeiraPalavra = input()
palavraAnterior = primeiraPalavra
palavraAtual = ""

qtdPalavraDiferente = 0

for i in range(qtdJogadores - 1):
    nome = input()
    palavraAtual = input()

    if palavraAtual != palavraAnterior:
        qtdPalavraDiferente += 1
        print(f"Parece que {nome} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
        if qtdPalavraDiferente == 5:
            print(f"Caramba, que confusão! A palavra {primeiraPalavra} já tá toda embaralhada e virou {palavraAtual}!")

        if qtdPalavraDiferente == 1: nomeErro1 = nome
        if qtdPalavraDiferente == 2: nomeErro2 = nome

    palavraAnterior = palavraAtual

if palavraAtual == primeiraPalavra:
    if qtdPalavraDiferente == 0:
        print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {primeiraPalavra}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
    else:
        print(f"Parece que ocorreram {qtdPalavraDiferente} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {primeiraPalavra} conseguiu chegar no fim do telefone sem fio.")
else:
    if qtdPalavraDiferente == 1:
        print(f"Poxa, foi por pouco, só quem errou foi {nomeErro1} que disse {palavraAtual} ao invés de {primeiraPalavra}…")
    elif qtdPalavraDiferente == 2:
        print(f"Se não fosse pelos erros de {nomeErro1} e {nomeErro2} a palavra {primeiraPalavra} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
    else:
        print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {primeiraPalavra} acabou virando {palavraAtual}. No total, ocorreram {qtdPalavraDiferente} trocas.")