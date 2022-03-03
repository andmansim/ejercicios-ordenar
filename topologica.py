#Variables
tareas = {1: {7, 3, 9}, 2: {4, 8}, 3: {6, 4},  4: {}, 5: {1}, 6: {}, 7: {}, 8: {}, 9: {2}}
tareas2=[[1,7],[1,3],[1,9],[2,4],[2,8],[3,6],[3,4],[4,"-"],[5,1],[6,"-"],[7,"-"],[8,"-"],[9,2]]
e_padre = []

#Nos lee el diccionario y los elementos padres nos lo apunta en una lista


for i in range(0,len(tareas2)-1):
    
    if tareas2[i][1] == "-":
        e_padre.append(tareas2[i][0])
print(e_padre)




"""
for a,b in tareas.items():
    m = 0
    r=len(b)
    for j in range(0,r):
        print (b[0])
        if b in e_padre:
            m = m + 1
            print(m)
        if m == len(b):
           e_padre.append(a)

print(e_padre) """