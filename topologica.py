#Variables
tareas = {1: [7, 3, 9], 2: [4,8], 3: [6,4], 4:[], 5: [1], 6:[], 7:[], 8:[],9: [2]} #lista de tareas y sus dependencias
t_ejecutada = [] # Lista donde se guardan las tareas ya ejecutadas
#Nos lee la lista y los elementos padres nos lo apunta en una lista
def ejecutarTarea(r):
    for j in tareas [r]:
        if j not in t_ejecutada:
            ejecutarTarea(j)
    t_ejecutada.insert(0, j)
            
for i in range(1,len(tareas)):
    if i not in t_ejecutada:
        ejecutarTarea (i)
   
print(t_ejecutada)
      
     
               
ejecutarTarea(1)
print(t_ejecutada)
     
    


            

     
    


            
    