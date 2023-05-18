#Verifica se a lestra inserida é uma vogal ou uma consoante

#Dados inseridos pelo usuário

x = input("Insira uma única letra para verificar se ela é vogal ou consoante: ")

#Função de verificação: Consoante ou vogal?

def eh_vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if x.lower() in vogais:
        return(bool(True))
    else:
        return(bool(False))

#Resultados

print(eh_vogal(x))