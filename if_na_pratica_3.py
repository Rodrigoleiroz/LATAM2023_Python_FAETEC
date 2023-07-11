# Como você certamente sabe, devido a algumas razões astronômicas, os anos podem ser bissextos ou comuns. Os primeiros têm 366 dias, enquanto os segundos têm 365 dias.

# Desde a introdução do calendário gregoriano (em 1582), a regra a seguir é usada para determinar o tipo de ano:

# se o número do ano não é divisível por quatro, é um ano comum;
# caso contrário, se o número do ano não for divisível por 100, será um ano bissexto;
# caso contrário, se o número do ano não for divisível por 400, é um ano comum ;
# caso contrário, é um ano bissexto .
# Observe o código no editor: ele só lê o número de um ano e precisa ser concluído com as instruções de implementação do teste que acabamos de descrever.

# O código deve gerar uma das duas mensagens possíveis, que são ano bissexto ou ano comum, dependendo do valor inserido.

# Seria bom verificar se o ano inserido cai na era gregoriana e emitir um aviso caso contrário: não está dentro do período do calendário gregoriano. Dica: use os operadores != E %.

# Teste seu código usando os dados que fornecemos.

ano = int(input("Digite um ano: "))

if ano < 1582:
  print("Não está dentro do período do calendário gregoriano")
  
elif ano % 4 != 0:
  print ( ano, "é um ano comum!")

elif ano % 100 != 0:
  print ( ano, "é um ano bissexto!") 

elif ano % 400 != 0:
  print ( ano, "é um ano comum!") 

else:
  print ( ano, "é um ano bissexto!")