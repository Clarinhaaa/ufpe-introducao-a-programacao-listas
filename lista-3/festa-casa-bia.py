listInfluencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
listCantores = ["Thiaguinho", "Little Thiago", "Neiff", "Diferenciado", "Veigh", "Mc Loma"]

nomeConvidado = ""
listConvidados = []
qtdInfluencers = 0
qtdCantores = 0

strInput = input()
if strInput == "WhatsApp: 0 mensagens.":
    print("I hate to tell you this BUT")
    print("Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")
    print()
    print("Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:")
    print("Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.")
    print("E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.")
    print("Espera esfriar e você vai barbarizar quando tiver pronto")
    print("É isso, tchau meus amores")
else:
    while strInput != "CABOSSE! Bora simbora organizar essa festa.":
        nomeConvidado = strInput.rsplit(" ", 3)[0]

        if nomeConvidado in listInfluencers: qtdInfluencers += 1
        else: qtdCantores += 1

        listConvidados.append(nomeConvidado)
        if nomeConvidado == "Mc Loma":
            listConvidados.append("Mirella Santos")
            listConvidados.append("Mariely Santos")
            
        strInput = input() # {convidado} acabou de confirmar
    
    if qtdInfluencers == 0: # só tem cantores
        print("<PLANOS PARA FESTA>")
        print(f'Convidados: {", ".join(listConvidados)}.')
        print("Tipo de comemoração: Paredão - Show na minha casa!!")
    elif qtdCantores == 0: # só tem influencers
        print("<TARDE DE FOFOCAS>")
        print(f'Convidados: {", ".join(listConvidados)}.')

        listPautas = []
        qtdPessoasConcordam = 0
        
        for i in range(len(listConvidados)):
            strInput = input()
            listPautas.append(strInput)

        for pauta in listPautas:
            if pauta == "Medo de ficar musculosa demais por causa da academia":
                print("AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!")
            elif pauta == "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?":
                print("Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)")
            elif pauta == "Meu chefe só me dá um dia de folga, mas eu precisava de dois.":
                print("Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!")
            elif pauta == "Pessoas que adoram se fazer de coitadinhas":
                print("Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.")
            else: # "Essa história de que homem sofre calado"
                print("Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???")

        qtdPessoasConcordam = int(input())
        if qtdPessoasConcordam == 0: print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else: print("É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")
    else: # tem um pouco dos dois
        print("Cachaçaria na minha casa hoje, 21h.")
        print("Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")