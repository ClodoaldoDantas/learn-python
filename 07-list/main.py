# Lists: Coleções ordenadas e mutáveis.
# Permitem modificação dinâmica de elementos.

print("Monte sua lista de frutas")

fruit = input("Digite o nome da fruta: ")
fruits = ["banana"]

while fruit.lower() != "q":
    fruits.append(fruit)
    fruit = input("Digite o nome da fruta: ")

print(f"Sua lista de frutas: {fruits}")
print(f"Quantidade: {len(fruits)} itens.")
