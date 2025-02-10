senha_correta = 'su123'
tentativa = ''

print ("Seja bem vindo, por favor digite sua senha: ")

while tentativa != senha_correta:
    tentativa = (input("digite sua senha: "))
    if tentativa != senha_correta:
        print ("Sua senha está incorreta!")
    else:
        print ("Logado com sucesso")
