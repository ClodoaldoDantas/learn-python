num = int(input("Deseja saber a tabuada de qual número? "))

if num >= 1 and num <= 9:
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")
else:
    print("Número inválido. Valores permitidos: 1 a 9")
