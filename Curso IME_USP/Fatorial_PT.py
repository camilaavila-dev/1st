#receba uma sequencia de números inseridos pelo usuario e para cada numero que ele digite vc vai imprimir o fatorial desse numero

n = int(input("Digite um número inteiro: "))
while n >= 0:
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    print(fat)
    n = int(input("Digite um número inteiro: "))
    


