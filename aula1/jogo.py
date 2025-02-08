print("Bem vindo ao Jogo")
print("Escolha um caminho:")
print("****************************************************")
print("1.Floresta Tortuoza")
print("2.Lago Enfeitiçado")
print("4.Sair do jogo")

escolha = int (input ("Qual caminho voce escolhe: "))

if escolha == 1 : 
    print ("Tome cuidado, encontre abrigo antes de anoitecer.")
    print("1.Procurar abrigo para se proteger")
    print("2.Pegar espada para se defender.")
    
    abrigo = int(input ("O que você prefere?"))

    if escolha == 1 :
        print ("Você encontrou uma caverna,tente descansar agora")
    else :
        print ("Escontre a espada e cuide-se")
    

elif escolha == 2 :
    print ("Converse com a sereia, ela te mostrará o caminho.")

else :
    print ("Jogo finalizado")