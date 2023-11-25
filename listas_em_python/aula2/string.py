
# operacoes 
# funcao len retorna o numero de caracter
# lower e uppercase 

nome = input("Digite o primeiro nome:  \n")
sobrenome = input("Digite o seu sobrenome:  \n")

tamanho = len(nome)
tamanho_sobre = len(sobrenome)

print("O comprimento do nome é: ", tamanho)
print("O comprimento do sobrenome é: ", tamanho_sobre)

nome = nome + " " + sobrenome
print("Apos concatenar as strings temos:", nome)

if sobrenome in nome:
    print("O sobrenome", sobrenome, "está contido no nome", nome, ".")
    
print("O nome completo em minusculo é: ", nome.lower())
print("O nome completo em maiusculo é: ", nome.upper())