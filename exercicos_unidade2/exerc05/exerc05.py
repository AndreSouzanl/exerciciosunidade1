peso = float(input("Digite a seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura * altura)
print("O imc é: ", IMC)

if IMC < 21.0:
    print("Abaixo do peso")
elif IMC >= 21.0 and IMC <= 30.75:
    print("peso padrao")
else:
    print("Acima do peso")

