num1, operador, num2 = int(input()), input(), int(input())
resultado = (num1 + num2) if operador == "+" else (num1 - num2) if operador == "-" else (num1 * num2) if operador == "*" else (num1 / num2)
print()