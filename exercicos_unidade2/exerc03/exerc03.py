
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não eleitor")
elif idade < 18 or idade > 65:
    print("eleitor facultativo")
else:
    print("Eleitor obrigatório")