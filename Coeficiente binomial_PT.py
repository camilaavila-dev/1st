#Nota: Eu sei da existência da função math comb, porém estou exercitando meu raciocínio através de exercícios simples.



#Dados inseridos pelo usuário

n = float(input("Insira o númerador - n: "))
k = float(input("Insira o denominador - k: "))

#Função fatorial

def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while (i <= n):
        fat = fat * i
        i = i + 1
    return fat

resultado = fatorial(n)

#Número binomial

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial((n-k)))
n! / (k! * (n - k)!)

#Teste

def test_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

#Resultado
        
print(resultado)