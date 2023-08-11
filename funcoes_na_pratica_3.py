# Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e 

# retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

# Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código.

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

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    res = days[month - 1] 

    if month == 2 and is_year_leap(year):
        res = 29  
    return res

def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12:
        return None
    
    md = days_in_month(year, month)
    
    if day >= 1 and day <= md:
        days = day  
        for m in range(1, month):
            days += days_in_month(year, m)
        return days
    else:
        return None

print(day_of_year(2001, 12, 31))
