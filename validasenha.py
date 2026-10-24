import random

rodar=True
letras="abcdefghijklmnopqrstuwyxz"
num="0123456789"
especial="!@#$%^&*()-+=/?"

senhas=letras+num+especial

while rodar==True:
    senha = input("Digíte uma senha: \n")

    if len(senha)<8:
        print("Senha inválida! A senha deve conter ao menos 8 caracteres. \n")
        
    elif senha.islower() or senha.isupper() or senha.isalpha() or senha.isnumeric():
        print("O nível de segurança da sua senha é: fraca! \n")

    elif senha.isupper() and senha.islower() or senha.isupper() and senha.isnumeric() or senha.islower() and senha.isnumeric() or senha.isnumeric() and senha.isupper() and senha.islower():
        print("O nível de segurança da sua senha é: média! \n")

    else:
        print("O nível de segurança da sua senha é: forte! \n")

    continuar = input("Deseja testar outra senha? (s/n) \n")
    if continuar == "n":
        break

gerador = input("Deseja ver sugestão de senha aleatória? (s/n) \n")

if gerador == "s":
    senha_aleatória="".join(random.choices(senhas, k=8))
    print(f"Senha forte sugerida: {senha_aleatória}")
else: 
    rodar=False

