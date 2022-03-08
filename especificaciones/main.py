import especificaciones

# Variables
t = [14, 7, 12, 6, 18, 13, 9, 10, 16, 21, 19, 8, 25, 3]
inicio = 0
fin = len(t) - 1
segmento = [] #se irá guardando los distintos segmentos que encontremos 

if __name__ == "__main__":
    segmento = especificaciones.segmentos(inicio, fin, t)
    print(segmento)
    