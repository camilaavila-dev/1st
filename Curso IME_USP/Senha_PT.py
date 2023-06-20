senha = input("Crie uma senha. ")
confirma = input("Confirme sua senha. ")
while senha != confirma:
    confirmedenovo = input("Senha incorreta, tente novamente. ")
    confirma = confirmedenovo
else:
    print("Senha correta.")