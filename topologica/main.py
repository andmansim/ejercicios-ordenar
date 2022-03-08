import funciones

#Variables
tareas = {1: [7, 3, 9], 2: [4,8], 3: [6,4], 4:[], 5: [1], 6:[], 7:[], 8:[],9: [2]} #lista de tareas y sus dependencias
t_ejecutada = [] # Lista donde se guardan las tareas ya ejecutadas

if __name__ == "__main__":
    for i in range(1,len(tareas)): #Recorre la primera parte del diccionario
        if i not in t_ejecutada: #Mira si la tarea está en ejecutada, si no está llama a la función ejecutarTarea para ver las subtareas y así ejecutarla
            funciones.ejecutarTarea(i, tareas, t_ejecutada)
                    
    t_ejecutada.reverse()
    print("Orden de las tareas")
    print(t_ejecutada)   