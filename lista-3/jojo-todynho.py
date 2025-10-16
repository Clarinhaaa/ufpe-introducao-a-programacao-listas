grimorio = ["Que tiro foi esse?", "Segura a marimba", "Tá com raiva? Morde as costas", "Bateu de frente é só rajadão"]

qtdNovasFrases = int(input())
novaFrase = ""

for i in range(4, qtdNovasFrases + 4):
    novaFrase = input()
    grimorio.append(novaFrase)

# cria uma lista nova sem repetição de termos
grimorioSemRepetir = []
for item in grimorio:
    if item not in grimorioSemRepetir:
        grimorioSemRepetir.append(item)

for item in grimorioSemRepetir:
    print(f'"{item}": {grimorio.count(item)}')

print(sorted(grimorio))