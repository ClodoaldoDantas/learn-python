print("Bem vindo a nossa calculador de gorjetas!")

bill = float(input("Qual foi o valor da conta? R$ "))
tip = int(input("Qual o valor da gorjeta que você gostaria de dar? 10, 12 ou 15 por cento? "))
people = int(input("Quantas pessoas devem dividir a conta? "))

total_tip = bill * (tip / 100)
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Cada pessoa deve pagar: R$ {final_amount}")
