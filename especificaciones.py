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
def explorar():
    t2 = [14, 7, 30, 12, 6, 18] #lista de prueba
    i = 0
    fin = len(t2)
    while i < fin - 1:
        if t2[i] > t2[i + 1]: #compara elementos con el siguente y pone el máximo al final
            t2[i], t2[i + 1] = t2[i + 1], t2[i]
        i = i + 1
    
    t2.insert(0, t2[len(t2) - 1]) #coloca el máximo al principio y mueve el resto una posición a la derecha
    del(t2[len(t2) - 1])
    print(t2)

explorar()
