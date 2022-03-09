#Primera parte del primer ejercicio
#Variables
tabla = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
tabla2 = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]

a = len(tabla)

#Función
def comparar(t2):
  
    for i in range(1, a): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t2[i]
        k = i   
                
        while  k > 0 and t2[k - 1] > inicial:
            t2[k] = t2[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t2[k] = inicial 
                
    return t2
         
#Segunda parte del primer ejercicio
#Variables
t1 = comparar(tabla)
print("tabla")
print(t1) #tabla ordenada
r = [None] * len(tabla)  #tabla auxiliar con el número de elementos que t


#Función ordenar con búsqueda dicotomía
def ordenar(t):
        
    for j in range(0, len(t)): #recorremos la lista tabla para poder ordenarla
        c = True  
        inicial = 0
        fin = len(t1)
        m = int((fin - inicial)/ 2) # dividimos a la mitad la lista tabla ya ordenada
        
        while c == True:
            if t[j] > t1[m + inicial]: #
                inicial = inicial + m    
                m =  int((fin - inicial)/ 2)
                 
            elif t[j] < t1[m + inicial]: 
                fin = fin - m 
                m = int((fin - inicial)/ 2)
              
            else:
                
                r[m + inicial] = t[j]
                print(r)
                c = False
            
ordenar(tabla2)