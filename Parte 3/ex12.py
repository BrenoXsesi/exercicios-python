soma = 0.0

while True: 
    numero = float(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    soma += numero

print(f"A soma dos números é: {soma:.2f}")


