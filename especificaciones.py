# Variables
t = [14, 7, 12, 6, 18, 13, 9, 10, 16, 21, 19, 8, 25, 3]
inicio = 0
fin = len(t) - 1
segmento = [] #se irá guardando los distintos segmentos que encontremos 
segmento_final = [] #mostrará el resultado final

# Función que divide en segmentos nuestra lista con el número máximo al principio
def segmentos ():
    segmento = []
    e = 0
    s_total = [] #lsita que contiene a todos los segmentos
    for k in range (i, fin + 1):
        if t[k] > t[i]:
            for j in range(i, k):
                segmento.append(t[j])
            s_total.append(segmento)
            segmento = []
            e = k
            i = k
            
    