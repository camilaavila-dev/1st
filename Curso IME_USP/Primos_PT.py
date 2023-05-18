#Verificar o maior número primo igual ou menor ao valor inserido

#Dados inseridos pelo usuário

k = int(input("Insira um número interio maior que 2: "))

def éPrimo(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True


def maior_primo(k):
    while k >= 2:
        if éPrimo(k):
            return k
        k -= 1
    return None


resultado = int(maior_primo(k))

print (resultado)
