#Variables
t = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]

a = len(t)

def comparar():
  
    for i in range(1, a ):
        inicial = t[i]
                       
        while  i > 0 and t[i -1] > inicial:
            t[i] = t[i - 1]
            i=i -1
            t[i] = inicial
            print (t)    
        print(t)
            

comparar()

