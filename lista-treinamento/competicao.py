dArthur = int(input())
dLuiz = int(input())
dPedro = int(input())
horas = int(input())

dArthur *= horas
dLuiz *= horas
dPedro *= horas

primeiroResultado = (dArthur + dLuiz + (abs(dArthur - dLuiz))) / 2
segundoResultado = (primeiroResultado + dPedro + (abs(primeiroResultado - dPedro))) / 2

print(int(segundoResultado))