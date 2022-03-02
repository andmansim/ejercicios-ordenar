#Variables
t = [2, 6, 7, 8, 3, 5, 1, 9, 0]
r = []

for i in range(1, len(t)): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
    inicial = t[i]
    k = i 
    if t[k - 1] > inicial:  #filtro para añadir solo al que ordenamos       
        while  k > 0 and t[k - 1] > inicial:
            t[k] = t[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t[k] = inicial 
            print("tabla t")
            print (t)    
            
        r.append(inicial)
        r.sort() #nueva tabla ordenada

    