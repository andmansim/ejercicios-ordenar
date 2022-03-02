#Variables
t = [2, 6, 7, 8, 3, 5, 1, 9, 0]
r = []
'''a = t.copy()
def comparar():
    for i in range(1, len(t)): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t[i]
        k = i 
        if t[k - 1] > inicial:  #filtro para añadir solo al que ordenamos       
            while  k > 0 and t[k - 1] > inicial:
                t[k] = t[k - 1]
                k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
                t[k] = inicial 
                
            #r.append(inicial)
            #r.sort() #nueva tabla ordenada
       # else: #añadimos los elementos que van en orden creciente y los ordenamos
            #r.append(t[k - 1])
        print (t)    
        r.append(t[i])        
   # if len(t) == len(r): #comprobación de que ambas listas tienen los mismos elementos
        #pass
    #else:
        #r.append(t[len(t) - 1])
    
comparar()

print("tabla t")
print (a)    
print("tabla r")
print(r)    
    '''
r = ['','','','','','','','','']    
for i in range (0, len(t)):
    m = 0
    for k in range(0, len(t)):
        #if t[i] < t[i - 1]:
           
        if t[k] < t[i]:
            #print(k)
            m = m + 1
                         
    print (m, t[i])
    r[m] = t[i]
    print (r)
    