# Recebendo os valores
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
valor3 = int(input("Digite mais um número: "))

# Inicio do código

maior_numero = valor1

if maior_numero < valor2:
    maior_numero = valor2

elif maior_numero < valor3:
    maior_numero = valor3

print ("O maior numero é igual a ", maior_numero)
