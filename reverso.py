num = int(input("Digite um número inteiro: "))
reverso = 0

while num > 0:
    resto = num % 10
    reverso = reverso * 10 + resto
    num = num // 10

print("O reverso do número é:", reverso)
