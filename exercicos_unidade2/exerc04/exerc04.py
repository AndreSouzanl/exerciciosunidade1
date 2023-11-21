
altura = float(input("Digite sua altura: "))
sexo = input("Digite M - masculino F - feminino: ")

if sexo == "F" or sexo == "f":
    peso = (61.2 * altura) - 44.7
    
else:
    peso = (72.1 * altura) - 58
    
print("O sexo é: " , sexo)
print("A altura é: ", altura)
print("O peso ideal é: ", peso)

