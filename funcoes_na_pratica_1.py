# Sua tarefa é escrever e testar uma função que usa um argumento (um ano) e retorna True se o ano for um ano bissexto ou False caso contrário.

# A semente da função já é semeada no código de esqueleto no editor.

# Nota: também preparamos um código de teste curto, que você pode usar para testar sua função.

# O código usa duas listas - uma com os dados de teste e a outra contendo os resultados esperados. O código informará se algum dos resultados é inválido.

def is_year_leap(year):
    
    if year < 1582:
        print("Não está dentro do período do calendário gregoriano")
        return False
        
  
    elif year % 4 != 0:
        print ( year, "é um ano comum!")
        return False
        

    elif year % 100 != 0:
        print ( year, "é um ano bissexto!") 
        return True
        

    elif year % 400 != 0:
        print ( year, "é um ano comum!") 
        return False
        
    else:
        print ( year, "é um ano bissexto!")
        return True
        

# is_year_leap(int(input("Digite o ano que deseja consultar: ")))
    


test_data = [1400, 1900, 2000, 2016, 1987]

test_results = [False, False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]

    print(yr,"->",end="")

    result = is_year_leap(yr)

    if result == test_results[i]:
        print("OK")

    else:
        print("Fracassado")