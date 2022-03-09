#Primera parte del primer ejercicio
#Variables
t = [6, 7, 2, 4, 1, 3, 9, 5, 8 ]
a = len(t)

#Función
def comparar():
  
    for i in range(1, a): #Empezamos con el 1 para poderlo comparar con el posterior y con el siguiente
        inicial = t[i]
        k = i           
        while  k > 0 and t[k - 1] > inicial:
            t[k] = t[k - 1]
            k = k - 1  #Hacemos que retroceda para no saltarnos ningún valor
            t[k] = inicial 
            print (t)    
        print(t)
         
#Segunda parte del primer ejercicio
#Variables
t1 = comparar()

r = [None] * len(t) #tabla auxiliar con el número de elementos que t


#Función
def ordenar():
    for j in range(0, len(t) - 1):
        
        b = int(len(t1) / 2)
        print(b)
        c = True
        while c == True:
            
            if t[j] > t1[b]:
                q = len(t1[b + 1], len(t1))
                pass
            elif t[j] > t1[b]:
                t2 = []
                for w in range(0, b):
                    t2.append(t1[w])
                    b = int(len(t2) / 2)
                    print(t2)
                    print(b)
                    c = True
            else: 
                r.insert(0, t[j])
                print(r)
                c = False
            