hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

 # Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário. 

insert_number = int(input("Digite um numero: "))

hat_list[2] = insert_number

print(hat_list)

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.

del hat_list[-1]

print(hat_list)

hat_list.append(777)

hat_list.insert(1, 666)

 # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual

print (len(hat_list))

print(hat_list)