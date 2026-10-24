import sys

print("Bem-vindo a nossa pizzaria")
size = input("Qual o tamanho da pizza? (P, M, G) ")

if size not in ("P", "M", "G"):
    print("Tamanho de pizza inválido")
    sys.exit()

pepperoni = input("Deseja adicionar pepperoni? (S ou N) ")
extra_cheese = input("Deseja uma camada extra de queijo? (S ou N) ")
total = 0

if size == "P":
    total += 15
elif size == "M":
    total += 20
elif size == "G":
    total += 25

if pepperoni == "S":
    if size == "P":
        total += 2
    else:
        total += 3

if extra_cheese == "S":
    total += 1

print(f"Valor total a pagar: R$ {total} reais")
