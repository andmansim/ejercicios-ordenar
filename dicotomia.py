#Primera parte del primer ejercicio
#Variables
t = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
a = len(t)

#Función
def comparar():
  
    for i in range(1, a): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t[i]
        k = i           
        while  k > 0 and t[k - 1] > inicial:
            t[k] = t[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t[k] = inicial 
            print (t)    
        print(t)
            



