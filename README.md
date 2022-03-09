# ejercicios-ordenar
Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/ejercicios-ordenar.git)

https://github.com/andmansim/ejercicios-ordenar.git

He realizado una serie de ejercicios mediente distintos métodos de ordenación, al igual que un diagrama de flujo y un UML.
El primer ejercicio consistía en una ordenación dicotómica. Se divide en dos partes:
Su diagrama de flujo es el siguiente:

![diagrama de flujo de dicotomia](/Dicotomia.jpg)

Y su UML es:

![diagrama UML de dicotomia](/dicotomia/UMLdicotomia.jpg)

```
#Main
import funciones
#Variables
tabla = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
tabla2 = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
r1 = [None] * len(tabla)  #tabla auxiliar con el número de elementos que t

if __name__ == "__main__":
    tabla1 = funciones.comparar(tabla)
    v = funciones.ordenar(tabla2, tabla1, r1)
 
 #Primera parte del primer ejercicio
#Función que compara los elementos y los ordena
def comparar(t2):
  
    for i in range(1, len(t2)): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t2[i]
        k = i   
                
        while  k > 0 and t2[k - 1] > inicial:
            t2[k] = t2[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t2[k] = inicial 
                
    return t2
    
#Parte de funciones       

#Segunda parte del primer ejercicio
#Función ordenar con búsqueda dicotomía
def ordenar(t, t1, r):
        
    for j in range(0, len(t)): #recorremos la lista tabla para poder ordenarla
        c = True  
        inicial = 0
        fin = len(t1)
        m = int((fin - inicial)/ 2) # dividimos a la mitad la lista tabla ya ordenada
        
        while c == True: #nos acotan el rango para poder comparar con el del medio
            if t[j] > t1[m + inicial]: 
                inicial = inicial + m    
                m =  int((fin - inicial)/ 2)
                 
            elif t[j] < t1[m + inicial]: 
                fin = fin - m 
                m = int((fin - inicial)/ 2)
              
            else:
                
                r[m + inicial] = t[j] #añade el elemento a la lista r en su posición correcta
                print(r)
                c = False
 ```


El segundo ejercicio, hemos hecho una ordenación topológica, donde unas tareas dependían de otras para que se ejecutasen.
Su diagrama de flujo es el siguiente:

![diagrama de flujo de topologica](/Topologica.jpg)

Y su UML es:

![diagrama uml de topologica](/topologica/UMLtopologica.jpg)

En el tercer ejercicio, hemos ordenado segmentos mediante una ordenación de especificaciones.
Su diagrama de flujo es el siguiente:

![diagrama de flujo de especificaciones](/Especificaciones.jpg)

Y su UML es:

![diagrama uml de especificaciones](/especificaciones/UMLespecificaciones.jpg)

```
#Main
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
    
#Funciones

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

```

