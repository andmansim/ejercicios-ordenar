import funciones

# Variables
tabla = [14, 7, 12, 6, 18, 13, 9, 10, 16, 21, 19, 8, 25, 3]
inicio = 0
f = len(tabla) - 1
segmento = [] #se irá guardando los distintos segmentos que encontremos 

if __name__ == "__main__":
    segmento = funciones.segmentos(inicio, f, tabla)
    print(segmento)
    segmento_final = funciones.ordenar(segmento) #mostrará el resultado final
    print(segmento_final)