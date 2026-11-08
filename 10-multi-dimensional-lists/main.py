fruits = ["Maçã", "Laranja", "Banana"]
vegetables = ["Cenoura", "Batata", "Brócolis"]
meats = ["Frango", "Carne Bovina", "Peixe"]

market = [fruits, vegetables, meats]

for category in market:
    for item in category:
        print(item, end=" ")
    print()
