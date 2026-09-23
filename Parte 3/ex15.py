positivo = 0

while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))

    if numero == 0:
        break

    if numero > 0:
        positivo += 1

print(f"teve {positivo} números positivos")
