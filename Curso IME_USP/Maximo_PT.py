#Devolve o maior número inteiro

#Dados inseridos pelo usuário

x = int(input("Insira o primeiro número inteiro: "))
y = int(input("Insira o segundo número inteiro: "))
z = int(input("Insira o terceiro número inteiro: "))

#Função para devolver o maior dos inteiros

def maximo(x, y, z):
    max(x, y, z)
    return (max (x, y, z))
    
resultado = maximo(x, y, z)

#Resultados

print(resultado)