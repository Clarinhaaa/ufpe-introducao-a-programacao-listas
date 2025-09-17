artSheldon = int(input())
artLeonard = int(input())
artRaj = int(input())
artHoward = int(input())

expSheldon = int(input())
expLeonard = int(input())
expRaj = int(input())
expHoward = int(input())

ptsSheldon = artSheldon * 2 + expSheldon * 3
ptsLeonard = artLeonard * 2 + expLeonard * 3
ptsRaj = artRaj * 2 + expRaj * 3
ptsHoward = artHoward * 2 + expHoward * 3

vencedor = ""

if ptsSheldon >= ptsLeonard and ptsSheldon >= ptsRaj and ptsSheldon >= ptsHoward:
    vencedor = "Sheldon"
elif ptsLeonard >= ptsRaj and ptsLeonard >= ptsHoward:
    vencedor = "Leonard"
elif ptsRaj >= ptsHoward:
    vencedor = "Raj"
else:
    vencedor = "Howard"

print(f"Pontuação final:\nSheldon: {ptsSheldon}\nLeonard: {ptsLeonard}\nRaj: {ptsRaj}\nHoward: {ptsHoward}")
print()
print(f"O cientista da semana é: {vencedor}")

if vencedor == "Sheldon":
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif vencedor == "Leonard":
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif vencedor == "Raj":
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
else:
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")