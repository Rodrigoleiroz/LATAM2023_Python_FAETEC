# Os Beatles foram um dos grupos de música mais populares dos anos 60, e a banda mais vendida na história. Algumas pessoas consideram que eles são o 
# ato mais influente da era do rock. Na verdade, eles foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.

# A banda passou por muitas mudanças na formação, culminando em 1962 com a formação de John Lennon, Paul McCartney, George Harrison e Richard Starkey 
# (mais conhecido como Ringo Starr).


# Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

# etapa 1: criar uma lista vazia chamada beatles;
# etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
# etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
# etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
# etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.


# etapa 1

beatles = []

print("Etapa 1:", beatles)


# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")


print("Etapa 2:", beatles)


# etapa 3



for i in range(2):
    novo_membro = input("Digite o nome do novo membro da banda: ")
    beatles.append(novo_membro)
    continue

print("Etapa 3:", beatles)


# etapa 4

del beatles[-1]
del beatles[-1]

print("Etapa 4:", beatles)

# passo 5

beatles.insert(0, "Ringo Starr")

print("Etapa 5:", beatles)



# testando o tamanho da lista

print ("o fabuloso", len(beatles))

