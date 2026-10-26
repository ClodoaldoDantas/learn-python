print("Calculadora básica")
print("[A] Adição")
print("[S] Subtração")
print("[M] Multiplicação")
print("[D] Divisão")

operation = input("Digite a letra da operação que deseja fazer: ").upper()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operation == "A":
    result = num1 + num2
    print(f"Resultado: {result}")
elif operation == "S":
    result = num1 - num2
    print(f"Resultado: {result}")
elif operation == "M":
    result = num1 * num2
    print(f"Resultado: {result}")
elif operation == "D":
    result = num1 / num2
    print(f"Resultado: {result}")
else:
    print("Operação inválida!")
