
lista = [10, 20, 30]

print("Listas originais: ", lista)

#Adiciona um elemento no final da array
lista.append(99)
print("Adicionando o 99: ", lista)

#Remove o ultimo elemento do array
aux = lista.pop()
print("Elemento removido: ", aux)

print("Resultado final: ", lista)

#Acessando atraves de sua posicao
print(lista)
lista[0] = 100
lista[1] = 99

print(lista)
