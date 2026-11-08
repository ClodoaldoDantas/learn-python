# Sets: Coleções NÃO ordenadas de elementos únicos.
# NÃO permitem elementos duplicados nem indexação direta.

print("Monte sua lista de frutas")

fruit = input("Digite o nome da fruta: ")
fruits_set = set()

while fruit.lower() != "q":
    fruits_set.add(fruit)
    fruit = input("Digite o nome da fruta: ")

print(f"Sua lista de frutas: {fruits_set}")
print(f"Quantidade: {len(fruits_set)} itens.")
