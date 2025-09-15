dias = int(input())
casas = int(input())

horas = dias * 3
ticksTotais = (horas * 3600) * 10
ticksPorCasa = int(ticksTotais / casas)

print(ticksPorCasa)