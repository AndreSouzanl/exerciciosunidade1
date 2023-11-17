numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))

opcao = int(input("Escolha: 1 - soma , 2 - subtracao, 3 - multiplicacao, 4 - divisao: "))

if opcao == 1:
    soma = numero_1 + numero_2
    print("A soma é: ", soma)

elif opcao == 2:
    subtracao = numero_1 - numero_2
    print("A subtracao é: ", subtracao)

elif opcao == 3:
    multiplicacao = numero_1 * numero_2
    print("A multiplicação é ", multiplicacao)

elif opcao == 4:
    divisao = numero_1 / numero_2
    print("A divisao é: ", divisao)
else:
    print("Opcao Inválida")
    
