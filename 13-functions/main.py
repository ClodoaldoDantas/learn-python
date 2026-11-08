def calculate_percentage(value, percentage=10):
    return value * (percentage / 100)

print("🧮 Calculadora de porcentagem")
num = float(input("Digite um valor: "))

# result = calculate_percentage(num)
result = calculate_percentage(value=num)

print(f"10% de {num:.2f} é igual a {result:.2f}")
