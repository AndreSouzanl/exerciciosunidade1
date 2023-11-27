
matriz = []

# i = linha 
# j = colunas

# 1 for representa a linha e coluna 0 a 2
for i in range(3):
    linha = []
    for j in range(3):
        print("Insira o lemento da linha ", i, "coluna", j)
        dado = int(input())
        linha.append(dado)
    matriz.append(linha)
    
for i in range(3):
    for j in range(3):
        print("O elemento da linha", i, "coluna", j, "è:", matriz[i][j])