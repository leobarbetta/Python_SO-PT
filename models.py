def imprime_texto():
    with open("C:\\Shared\\teste.txt") as arquivo:
        linhas = arquivo.read().split("\n")
    for linha in linhas:
        linha = linha.strip("-")
        print(linha.strip(), end="")
imprime_texto()