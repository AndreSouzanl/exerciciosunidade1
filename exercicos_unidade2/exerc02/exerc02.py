
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <= 18:
    print("Valor plano de Saúde é de R$ 50,00")
elif idade >= 19 and idade <= 29:
    print("valor plano de Saude é de R$ 70,00")
elif idade >= 30 and idade <= 45:
    print("O valor do plano de saude e de R$ 90,00")
elif idade >= 46 and idade <= 65:
    print("O valor do plano de saude é de R$ 130,00")
else:
    print("valor do plano de Saúde é de R$ 170,00")