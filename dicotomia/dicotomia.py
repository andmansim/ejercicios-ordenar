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
    
    for j in range(0, len(t) - 1): #recorremos la lista tabla para poder ordenarla
        inicial = 0
        fin = len(t1)
        b = int(len(t1) / 2) # dividimos a la mitad la lista tabla ya ordenada
        print(b)
        c = True
        while c == True:
            
            if t[j] > t1[b]:
                inicial = b 
                b = inicial + int((fin - inicial)/ 2)
                print(b)
                c = True
            elif t[j] < t1[b]:
                b = int(b - 1 / 2)
                print(b)
                c = True
            else:
                v = t1.index(t1[b]) 
                r.insert(v, t[j])
                print(r)
                c = False
            
ordenar(tabla)