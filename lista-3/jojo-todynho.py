grimorio = ["Que tiro foi esse?", "Segura a marimba", "Tá com raiva? Morde as costas", "Bateu de frente é só rajadão"]

qtdNovasFrases = int(input())
novaFrase = ""

for i in range(4, qtdNovasFrases + 4):
    novaFrase = input()
    grimorio.append(novaFrase)

# cria uma lista nova sem repetição de termos
grimorioSemRepetir = []
for frase in grimorio:
    if frase not in grimorioSemRepetir:
        grimorioSemRepetir.append(frase)

for frase in grimorioSemRepetir:
    print(f'"{frase}": {grimorio.count(frase)}')

print(sorted(grimorio))