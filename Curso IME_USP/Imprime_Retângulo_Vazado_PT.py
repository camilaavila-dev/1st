largura = int(input("Insira a largura do retângulo: "))
altura = int(input("Insira a altura do retângulo: "))

linha = 0
coluna = 0
vazado = (largura - 2)

while linha < altura:
    while coluna < largura:
        if linha == 0 or linha == altura - 1 or coluna == 0 or coluna == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 0



