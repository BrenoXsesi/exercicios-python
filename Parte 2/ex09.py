nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("O aluno esta aprovado")
elif media >= 4 and media <= 5.9:
    print("O aluno esta em recuperação")
else:
    print("O aluno esta reprovado")