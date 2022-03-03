#Variables
tareas2=[[1,7],[1,3],[1,9],[2,4],[2,8],[3,6],[3,4],[4,"-"],[5,1],[6,"-"],[7,"-"],[8,"-"],[9,2]]
dependencias =[[1,3],[2,2],[3,2],[4,0],[5,1],[6,0],[7,0],[8,0],[9,1]]

t_ejecutada = [None] * len(tareas2)
#Nos lee la lista y los elementos padres nos lo apunta en una lista
num_tarea=0
for i in range(0,len(tareas2)-1):
    
    if tareas2[i][1] == "-":
        t_ejecutada.insert(num_tarea,tareas2[i][0])
        num_tarea = num_tarea + 1
print(t_ejecutada)
c = 0
print (tareas2.index (tareas2[2],[8]))
def ejecutarTarea(r, c,num_tarea):
    #tarea_ejecutar=tareas2[r][0]
    
    if tareas2[r][1] in t_ejecutada and c == dependencias[r][1]:
        #buscamos a siguiente dependencia
        #ejecutarTarea (r+1)
        #c=c+1
        
        t_ejecutada.insert(num_tarea,tareas2[r][0])
        num_tarea = num_tarea + 1
        
        
    elif num_tarea < 8: 
       #ejecutarTarea (r+1, c + 1,num_tarea)
       #c = c + 1
       r2 = tareas2.index (tareas2[r][1])
       ejecutarTarea (r2,c+1,num_tarea)
        
ejecutarTarea(0, 0,num_tarea)
print(t_ejecutada)
     
    


            