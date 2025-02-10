#frutas = ['Maça', 'Pera', 'Banana', 'Abacaxi',]

# adiciona um novo item na lista
#frutas.append('laranja')

#Tira um item da lista
#frutas.remove('Pera')

#for fruta in frutas:
 #  print(fruta)

alunos = []

while True:
   aluno =(input("Adicione o nome dos alunos ou sair: "))
   if aluno.lower() == 'sair':
      break

   alunos.append(aluno)

print("Lista de Presença: ")
for aluno in alunos:
   print(aluno)

