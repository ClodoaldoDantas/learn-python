import random

options = ("pedra", "papel", "tesoura")
computer_choice = random.choice(options)
user_choice = input("Escolha pedra, papel ou tesoura: ")

if user_choice in options:
    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")

    if user_choice == computer_choice:
        print("Empate! 🥸")
    elif (
        (user_choice == "pedra" and computer_choice == "tesoura")
        or (user_choice == "papel" and computer_choice == "pedra")
        or (user_choice == "tesoura" and computer_choice == "papel")
    ):
        print("Parabéns, você venceu! 🏆")
    else:
        print("Você perdeu! 😭")
else:
    print("Você digitou um valor inválido.")
