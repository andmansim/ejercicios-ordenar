#Variables
tareas = {1: {7, 3, 9}, 2: {4, 8}, 3: {6, 4},  4: {}, 5: {1}, 6: {}, 7: {}, 8: {}, 9: {2}}
e_padre = []
#Nos lee el diccionario y los elementos padres nos lo apunta en una lista
def buscar_padre():
    for i, k in tareas.items():
        print(len(k))
        print(i)
        if len(k) == 0:
            e_padre.append(i)
    print(e_padre)
    
buscar_padre