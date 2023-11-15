numero1 = float(input("Digite o numero 1:"))
numero2 = float(input("Digite o numero 2:"))
numero3 = float(input("Digite o numero 3: "))

peso1 = float(input("Digite o peso 1:"))
peso2 = float(input("Digite o peso 2:"))
peso3 = float(input("Digite o peso 3:"))


soma_pesos = peso1 + peso2 + peso3
media_ponderada = (numero1 * peso1) + (numero2 * peso2) + (numero3 * peso3) / soma_pesos

print("A Média Ponderada é: ", media_ponderada)

