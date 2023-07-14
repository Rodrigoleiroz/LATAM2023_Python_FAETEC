blocos = int(input("Digite o número de blocos: "))

altura = 0
camadas = 0

while blocos >= camadas + 1:
    camadas += 1
    blocos -= camadas
    altura += 1

print("A altura da pirâmide é:", altura)

    