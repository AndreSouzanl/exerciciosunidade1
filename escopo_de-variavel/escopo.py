
# raio = 0

# def areaCirculo():
#     return 3.14*raio**2

def areaCirculo(r):
    return 3.14*r**2

raio = float(input("Digite o raio do triangulo: "))

area = areaCirculo(raio)

print("A area do triângulo é: ", area)

