import re
senha = input("Crie uma senha.\n Regras: \n -A senha deve ter no mínimo 6 caracteres. \n -A senha deve ter no máximo 12 caracteres. \n -A senha deve ter pelo menos 1 letra minúscula e 1 letra maiúscula. \n -A senha dever ter pelo menos 1 número. \n -A senha deve ter pelo menos um caractere especial. [$#@] \n")

x = True

while x:
    if (len(senha)<6 or len(senha)>12):
        break
    elif not re.search("[a-z]", senha):
        break
    elif not re.search("[0-9]", senha):
        break
    elif not re.search("[A-Z]", senha):
        break
    elif not re.search("[$#@]", senha):
        break
    elif re.search("\s", senha):
        break
    else:
        print("Senha válida!")
        x = False
        break

if x:
        print("Senha inválida.\n")