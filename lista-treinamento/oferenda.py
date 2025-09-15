diamantes = int(input())

if diamantes <= 10:
    print("Arthur")
elif diamantes > 10 and diamantes <= 30:
    print("Luiz")
elif diamantes > 30 and diamantes < 100:
    print("Pedro")
else:
    print("Nenhum")