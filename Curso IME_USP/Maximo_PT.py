#Devolve o maior número inteiro

#Dados inseridos pelo usuário

x = int(input("Insira o primeiro número inteiro: "))
y = int(input("Insira o segundo número inteiro: "))

#Função para devolver o maior dos inteiros

def maximo(x, y):
    if x >= y:
        return x
    if y > x:
        return y
    
resultado = maximo(x, y)

#Resultados

print(resultado)