# Pergunta 1: Crie um loop for com contagem de 0 a 10 e imprima números ímpares na tela. Use o esqueleto abaixo:

for i in range(1, 11):
    if i % 2 != 0:
        print (i)

# Pergunta 2: Crie um loop while que conta de 0 a 10 e imprime números ímpares na tela. Use o esqueleto abaixo:

x = 1

while x < 11:
    if x % 2 != 0:
       print (x)

    x += 1

# Pergunta 3: Crie um programa com um loop for e uma declaração de break. O programa deve iterar os caracteres em um endereço de e-mail,
#  sair do loop quando atingir o símbolo @ e imprimir a peça antes de @ em uma linha. Use o esqueleto abaixo:

email = input("Digite seu email: ")

for ch in email:
    if ch == "@":
        break
    print(ch, end="")

# Pergunta 4: Crie um programa com um loop for e uma declaração continue. O programa deve repetir uma sequência de dígitos, 
# substituir cada 0 por x e imprimir a sequência modificada na tela. Use o esqueleto abaixo:


sequencia_digitos = input("Digite uma sequencia de numeros: ")

for digit in sequencia_digitos:
    if digit == "0":
        print("x", end="")
        continue

    print(digit, end="")


