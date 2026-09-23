preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))

soma_total = preco_produto * quantidade_produto

print(f"O valor total da compra é: R$: {soma_total:.2f}")