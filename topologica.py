#Variables
tareas = {1: [7, 3, 9], 2: [4,8], 3: [6,4], 4:[], 5: [1], 6:[], 7:[], 8:[],9: [2]} #lista de tareas y sus dependencias
t_ejecutada = [] # Lista donde se guardan las tareas ya ejecutadas
#Nos lee la lista y los elementos padres nos lo apunta en una lista
num_tarea=0
for i in range(0,len(tareas)-1):
    
    if tareas[i][1] == "-":
        t_ejecutada.insert(num_tarea,tareas[i][0])
        num_tarea = num_tarea + 1
print(t_ejecutada)
c = 0

def ejecutarTarea(r, c,num_tarea):
    #tarea_ejecutar=tareas2[r][0]
    
    if tareas[r][1] in t_ejecutada and c == dependencias.get(r):
        #buscamos a siguiente dependencia
        #ejecutarTarea (r+1)
        #c=c+1
        
        t_ejecutada.insert(num_tarea,tareas[r][0])
        num_tarea = num_tarea + 1
       
     
    elif num_tarea < 8: 
       #ejecutarTarea (r+1, c + 1,num_tarea)
       #c = c + 1
       r2 =dependencias.get(r)
       ejecutarTarea (r2,c+1,num_tarea)
     
        
ejecutarTarea(0, 0,num_tarea)
print(t_ejecutada)
     
    


            

     
    


            
    