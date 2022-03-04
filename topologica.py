#Variables
tareas = {1: [7, 3, 9], 2: [4,8], 3: [6,4], 4:[], 5: [1], 6:[], 7:[], 8:[],9: [2]} #lista de tareas y sus dependencias
t_ejecutada = [] # Lista donde se guardan las tareas ya ejecutadas
#Nos lee la lista y los elementos padres nos lo apunta en una lista

def ejecutarTarea(r): #Esta función recorre la segunda parte del diccionario, viendo así las tareas que depende
    for j in tareas[r]:
        if j not in t_ejecutada: # Si la subtarea no está ejecutada, se vuelve a llamar para comprobar las siguientes
            ejecutarTarea(j)
    t_ejecutada.insert(0, r) #Como si está ejecutada, la añade a la lista de t_ejecuta
            
for i in range(1,len(tareas)): #Recorre la primera parte del diccionario
    if i not in t_ejecutada: #Mira si la tarea está en ejecutada, si no está llama a la función ejecutarTarea para ver las subtareas y así ejecutarla
        ejecutarTarea(i)
                  
t_ejecutada.reverse()
print(t_ejecutada)   
    


            

     
    


            
    