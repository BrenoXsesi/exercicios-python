maior = 0.0
numeros = [5, 12, 8, 20, 3, 15]

for numero in numeros:
    if numero > 10:
        maior += 1

print(f"Quantidade de números maiores que 10: {maior}")