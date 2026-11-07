import datetime

print("Bem-vindo ao nosso cinema.")
print("Hoje teremos a estreia de Deadpool!")

year_of_birth = int(input("Em que ano você nasceu ? "))
current_year = datetime.date.today().year
age = current_year - year_of_birth

if age >= 18:
    print("Você pode assistir o filme. Aproveite!")
else:
    print("Desculpe, o filme é para maiores de 18 anos.")
