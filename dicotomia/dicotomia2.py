#Segunda parte del primer ejercicio
#Variables
t = [2, 6, 7, 8, 3, 5, 1, 9, 0]
r = [None] * len(t) #tabla auxiliar con el número de elementos que t


#Función
def ordenaaux():
    
    for i in range (0, len(t) - 1):
        m = 0
        for k in range(0, len(t)):
        
            if t[k] < t[i]: #Vemos los elementos menores que el que comparamos
                m = m + 1 
                            
        r[m] = t[i] #añadimos los elementos en sus respectivas posicones
        print (r)
ordenaaux()