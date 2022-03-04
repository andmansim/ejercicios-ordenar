#Variables
tareas = {1: [7, 3, 9], 2: [4,8], 3: [6,4], 4:[], 5: [1], 6:[], 7:[], 8:[],9: [2]} #lista de tareas y sus dependencias
t_ejecutada = [] # Lista donde se guardan las tareas ya ejecutadas
#Nos lee la lista y los elementos padres nos lo apunta en una lista


def ejecutarTarea():
    for j in tareas():
        if j not in t_ejecutada:
            ejecutarTarea(j)
        print(t_ejecutada)
 
def buscar(w):           
    for i in tareas[w]:
        if i not in t_ejecutada:
            buscar(i)
    print(t_ejecutada)


               
ejecutarTarea(0)
print(t_ejecutada)
     
    


            

     
    


            
    