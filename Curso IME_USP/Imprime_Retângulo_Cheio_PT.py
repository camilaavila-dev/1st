largura = int(input("Insira a largura do retângulo: "))
altura = int(input("Insira a altura do retângulo: "))

linha = 0
coluna = 0

while linha < altura:
    while coluna < largura:
        print("#", end="")
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 0
