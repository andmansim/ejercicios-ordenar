import funciones
#Variables
tabla = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
tabla2 = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
r1 = [None] * len(tabla)  #tabla auxiliar con el número de elementos que t

if __name__ == "__main__":
    tabla1 = funciones.comparar(tabla)
    v = funciones.ordenar(tabla2, tabla1, r1)
    