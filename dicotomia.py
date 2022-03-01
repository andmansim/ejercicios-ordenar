#Variables
t = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
a = len(t)

def comparar():
  
    for i in range(1, a): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t[i]
                       
        while  i > 0 and t[i - 1] > inicial:
            t[i] = t[i - 1]
            i = i - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t[i] = inicial 
            print (t)    
        print(t)
            

comparar()

