art = r"""
     /\_/\
    ( o.o )
     > ^ <
    """

print(art)
print("Bem-vindo à Ilha do Tesouro. Sua missão começa agora!")

first_choice = input("Deseja ir andando pela esquerda ou direita? (left or right): ")

if first_choice == "left":
    second_choice = input("Chegamos perto do mar. Deseja ir nadando ou esperar um barco? (swim or wait): ")

    if second_choice == "wait":
        third_choice = input("Chegamos no final do nosso destinho. Qual porta você escolhe? (red, blue or yellow): ")

        if third_choice == "red":
            print("Queimado pelo fogo. Fim de jogo.")
        elif third_choice == "blue":
            print("Comido por feras. Fim de jogo.")
        elif third_choice == "yellow":
            print("Você venceu, Parabéns!")
        else:
            print("Porta errada. Fim de jogo.")

    else:
        print("Atacado por trutas. Fim de jogo.")

else:
    print("Caiu em um buraco. Fim de jogo.")
