
# criacao do dicionario
produto = {
    'codigo': 0,
    'descricao': "",
    'preco': 0.0,
    'quantidade': 0.0,
}

# inserindo dados no dicionario
produto ['codigo'] = int(input("Digite o código do produto: \n"))
produto ['descricao'] = input("Digite a descrição do produto: \n")
produto ['preco'] = float(input("Digite o preço do produto: \n"))
produto ['quantidade'] = float(input("Digite a quantidade do produto: \n"))

# imprimindo os dados do dicionario
print("código: ", produto['codigo'])
print("Descrição: ", produto['descricao'])
print("Preço R$: ", produto['preco'])
print("Quantidade: ", produto['quantidade'])