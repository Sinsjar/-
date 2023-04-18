x = int(input())
p_inf = float('inf')
n_inf = float('-inf')
if(x > n_inf and x < -5):
    print("Принадлежит (-inf, -5)")
    
elif(x > -5 and x <= 5):
    print("Принадлежит (-5, 5)")
    
elif(x < 5 and x < p_inf):
    print("Принадлежит (5, +inf)")
    
else:
    print("Это значение не принадлежит никакому из интервалов")
