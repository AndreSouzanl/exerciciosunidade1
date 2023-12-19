
numero = int(input("Digite um numero: "))

qtde = 0

for i in range(1, numero+1, 1):
    if numero % i == 0:
        qtde += 1
if qtde == 2:
    print("Esse é um numero primo.")
else:
    print("Esse nao é um numero primo. ")