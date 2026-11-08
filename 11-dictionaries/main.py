capitals = {
    "Brasil": "Brasília",
    "EUA": "Washington D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
}

# add new item
capitals.update({"Alemanha": "Berlim"})

# update item
capitals.update({"Brasil": "Brasília (DF)"})

# remove item
capitals.pop("EUA")

for country, city in capitals.items():
    print(f"País: {country}", end=", ")
    print(f"Capital: {city}")
