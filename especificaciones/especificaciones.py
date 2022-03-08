
# Función que divide en segmentos nuestra lista con el número máximo al principio
def segmentos (i, fin, t):
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
    return s_total


            
         
#Función que coloca el elemento máximo de cada segmento al principio
def explorar(t):
    
    i = 0
    fin = len(t)
    while i < fin - 1:
        if t[i] > t[i + 1]: #compara elementos con el siguente y pone el máximo al final
            t[i], t[i + 1] = t[i + 1], t[i]
        i = i + 1
    
    t.insert(0, t[len(t) - 1]) #coloca el máximo al principio y mueve el resto una posición a la derecha
    del(t[len(t) - 1])
    return t



#Función que nos va a ordenar los elementos del segmento

def ordenar(segmento):
    subsegmento = [] #se almacenan los subsegmentos
    subsegmento2 = [] #subsegmento ordenado
    segmento_final = [] #mostrará el resultado final

    for m in range(0, len(segmento)):
        subsegmento = segmento[m] #se coge cada uno de los subsegementos
        while len(subsegmento) > 1:
            t_max = subsegmento[0] #el número máximo del segmento
            subsegmento2.insert(0, t_max) #inserta al principio el máximo en la lista donde se van a quedar ya todos ordenados
            del subsegmento[0]
            subsegmento = explorar(subsegmento) #le llamamos para que nos ponga el valor más alto al principio
        t_max = subsegmento[0]
        subsegmento2.insert(0, t_max)
        
        #ordenamos subsegmentos
        segmento_final.append(subsegmento2)
        subsegmento2 = []
    return segmento_final

        