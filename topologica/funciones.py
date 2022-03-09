
#Nos lee la lista y los elementos padres nos lo apunta en una lista
def ejecutarTarea(r, t, t_e): #Esta función recorre la segunda parte del diccionario, viendo así las tareas que depende
    for j in t[r]:
        if j not in t_e: # Si la subtarea no está ejecutada, se vuelve a llamar para comprobar las siguientes
            ejecutarTarea(j, t, t_e)
    t_e.insert(0, r) #Como si está ejecutada, la añade a la lista de t_ejecuta
            
