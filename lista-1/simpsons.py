nome = input()
ano = int(input())

print("Ativando a máquina...")

if ano % len(nome) == 0:
    if nome.lower() == "frink":
        print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!")
else:
    if nome.lower() == "frink":
        print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
    else:
        print(f"Previsão instável! {nome.capitalize()} também deve achar que o rebigulador é ridículo...")