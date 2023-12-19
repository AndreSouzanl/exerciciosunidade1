
lista = []

for i in range(5):
    pessoa = {
        "nome": "",
        "telefone": "",
     }
    
    pessoa['nome'] = input("digite seu nome: ")
    pessoa['telefone'] = int(input("digite seu telefone: "))
    
    lista.append(pessoa)
    
for j in range(5):
    print("Nome: ", lista[j]['nome'])
    print("tel: ", lista[j]['telefone'],"\n")

