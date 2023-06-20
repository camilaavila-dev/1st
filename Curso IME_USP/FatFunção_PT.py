#recebe uma sequência de números inseridos pelo usuário e para cada número que ele digita imprime o fatorial desse número

#Função
def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    print(fat)

n = int(input("Digite um número inteiro: "))
while n >= 0:
    fatorial(n)
    n = int(input("Digite um número inteiro: "))