print ('\t Sequência de Fibonacci')
n = int(input("Quantos termos da sequência de Fibonacci você quer?"))

num1 = 0
num2 = 1
contador = 0

while contador < n:
    num3= num1 + num2
    num1 = num2
    num2 = num3
    contador += 1
    print(num1)