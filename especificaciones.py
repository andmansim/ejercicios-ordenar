# Variables
t = [14, 7, 12, 6, 18, 13, 9, 10, 16, 21, 19, 8, 25, 3]
inicio = 0
fin = len(t) - 1
segmento = [] #se irá guardando los distintos segmentos que encontremos 
segmento_final = [] #mostrará el resultado final

# Función que divide en segmentos nuestra lista con el número máximo al principio
def segmentos (i):
    segmento = []
    e = 0
    s_total = [] #lista que contiene a todos los segmentos
    for k in range (i, fin + 1):
        
        if t[k] > t[i]: # solo pasa aquellos que son mayor que el primero
            
            for j in range(i, k): # los añadimos a segmento
                segmento.append(t[j])
                
            s_total.append(segmento) # añadimos el segmento al total
            segmento = []
            
            e = k # nos guarda el último valor de k para luego empezar con él
            i = k
        
        if k == fin: #añade los sobrantes
            segmento = []
            
            for g in range (e, fin + 1):
                segmento.append(t[g])
                
            s_total.append(segmento)
    print(s_total)

segmentos(inicio)
            
#esta función nos servirá para otra que nos ordenará los elementos de cada segmento          
#Función que coloca el elemento máximo de cada segmento al principio
def explorar(t):
    #t2 = [14, 7, 30, 12, 6, 18] #lista de prueba
    i = 0
    fin = len(t)
    while i < fin - 1:
        if t[i] > t[i + 1]: #compara elementos con el siguente y pone el máximo al final
            t[i], t[i + 1] = t[i + 1], t[i]
        i = i + 1
    
    t.insert(0, t[len(t2) - 1]) #coloca el máximo al principio y mueve el resto una posición a la derecha
    del(t[len(t) - 1])
    print(t)



#Función que nos va a ordenar los elementos del segmento

def ordenar(segmento):
    subsegmento = [] #se almacenan los subsegmentos
    subsegmento2 = [] #subsegmento ordenado
    for m in range(0, len(segmento)):
        subsegmento = segmento[m] #se coge cada uno de los subsegementos
        while len(subsegmento) > 1:
            t_max = subsegmento[0] #el número máximo del segmento
            subsegmento2.insert(0, t_max) #inserta al principio el máximo en la lista donde se van a quedar ya todos ordenados
            del subsegmento[0]
            subsegmento = explorar(subsegmento) #le llamamos para que nos ponga el valor más alto al principio
        print(subsegmento)
ordenar(segmento)
        