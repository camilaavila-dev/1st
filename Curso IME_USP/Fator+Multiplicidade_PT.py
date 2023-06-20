# Dado um número inteiro n, sendo que n é maior que 1, imprimir a sua decomposição em fatores primos, indicando também a multiplicidade de cada fator.
# Exemplos:
# 8 = 2 * 2 * 2 -> Fator único (2) Multiplicidade (3)
# 20 = 2 * 2 * 5 -> Dois fatoes (2 e 5) Multiplicidade do 2 = 2 e multiplicade do 5 = 1
# 1000 = 2^3 * 5^3 -> Dois fatores (2 e 3) Multiplicidade do 2 = 3 e multiplicade do 5 = 3

n = int(input("Digite um número inteiro maior que 1:"))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    print ("Fator=",fator, "e multiplicade =", multiplicidade)
    fator = fator + 1