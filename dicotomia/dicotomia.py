#Primera parte del primer ejercicio
#Variables
tabla = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
a = len(tabla)

#Función
def comparar(t):
  
    for i in range(1, a): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t[i]
        k = i   
                
        while  k > 0 and t[k - 1] > inicial:
            t[k] = t[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t[k] = inicial 
                
    return t
         
#Segunda parte del primer ejercicio
#Variables
t1 = comparar(tabla)
print("tabla")
print(t1)

r = [None] * len(tabla) #tabla auxiliar con el número de elementos que t


#Función
def ordenar(t):
    inicial = 0
    fin = len(t1)
    m = int((fin - inicial)/ 2) # dividimos a la mitad la lista tabla ya ordenada
    print(m)
    
    #for j in range(inicial, fin - 1): #recorremos la lista tabla para poder ordenarla
    for j in range(inicial, inicial): #recorremos la lista tabla para poder ordenarla
 
        c = 0  
        print(inicial,fin,m,t[j],t1[m + inicial] )
        while c < 4:
            if t[j] > t1[m + inicial]:
                inicial = inicial + m + 1   
                m =  int((fin - inicial)/ 2)
                print(inicial,fin,m,t[j],t1[m + inicial] )
                
                c = c + 1
                
            
            elif t[j] < t1[m + inicial]: 
                fin = m - 1 
                m = int((fin - inicial)/ 2)
                print(inicial,fin,m,t[j],t1[m + inicial] )
                c = c + 1
            
            else:
                v = t1.index(t1[m + inicial]) 
                r.insert(v, t[j])
                print(r)
                c = c + 1
            
ordenar(tabla)