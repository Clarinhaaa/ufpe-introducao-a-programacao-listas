altura = int(input())
linha = ""

"""
for i in range(altura): # para cada linha
    linha = ""
    for j in range((altura * 2) - 1): # para cada caractere de cada linha
        linha += "#" if j <= (altura - 1) + i and j >= (altura - 1) - i else "⠀"
    print(linha)
"""

for i in range(altura): # para cada linha
    linha = ""
    for j in range(altura + 1 + i): # para cada caractere de cada linha
        linha += "⠀" if j <= altura - 1 - i else "#"
    print(linha)