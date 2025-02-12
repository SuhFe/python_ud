print("Bem vindo ao Jogo")

inventario = []

#usar um loop for com  numero grande de iteracoes para simular um jogo continuo
while True:

    print("1.Cabana")
    print("2.Floresta")
    print("3.Ver inventário")
    print("4.Sair do jogo")

    escolha = int(input("Qual caminho voce escolhe: "))

    if escolha == 1 : 
        print ("A cabana tem uma espada.")
        print("1. Pegar a espada")
        print("2. Ignorar a espada.")
        print("3. Voltar para a floresta.")
            
        espada = int(input ("O que você faz?"))

        if espada == 1:
            inventario.append('espada')
            print("O jogador conseguiu uma espada.")
        elif espada == 2:
            print("Seu inventario está vazio")
        elif espada == 3:
            print("Voce voltou para a floresta")
        else :
            print("Número inválido!")

    elif escolha == 2 :
        print("Voce está na floresta escura.")

    elif escolha == 4 :
        print("Jogo finalizado")
        break
    
    elif escolha == 3 :
        print ("seu inventario")
        for item in inventario:
            print(f'{item}')