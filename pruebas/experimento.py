from math import ceil,log2

from functools import reduce

def get_data(nombre):
    data_arritmia = []
    with open(nombre,"r") as data:
        data = data.readlines()
    i = 0
    for d in data:
        aux_data = []
        bandera = 0
        for fact in d.split(","):
            if fact == "?":
                fact = 0
                bandera += 1
                if bandera == 2:
                    break
            aux_data.append(float(fact))
        
        if bandera !=2:
            data_arritmia.append(aux_data)
            i+=1

    return data_arritmia

def entropy(rows):
    columns = {} 
    entropies = []
        
    p = {} #las veces que aparecen las clases 
    s = []
    S = 0
    variables = len(rows[0])-1
    datos = len(rows)
    classes = []

    for row in rows:
        if not row[-1] in p:
            p[row[-1]]  = [0,0]
        p[row[-1]][0] += 1

    total = 0
    
    for apper in p.values():
        apper[1] = -(apper[0]/datos)*log2(apper[0]/datos)
        total = total + apper[1]
    p["E"] = total

    for r in range(variables):
        columns[r] = {}

    for row in rows:
        i = 0
        for c in columns.values(): #todas las columnas
            if not row[i] in c:
                c[row[i]] = {}
            if not row[-1] in c[row[i]]:
                c[row[i]][row[-1]] = 0
            c[row[i]][row[-1]] +=1      
            i+=1
    
    for values in columns.values():
        #column es la columna, cada columna tiene sus propios valores, organizados por 
        #cada value tiene los datos de cada columna son un dictado, donde cada uno tiene sus veces
        #que aparee en con cada clase.
        #primero toma la columna 1
        i = 0

        for dato,v in values.items():
            #dato es el dato de esa columna y v es el numero de veces que aparece en las clases
            total = 0
            v["E"] = 0
            
            #total de veces que aparece con una clase
            for clase in v.values():
                total = total+clase  
            v["T"] = total
            for clase in v:
                if clase == "E":
                    break
                v["E"] = v["E"] - (v[clase]/v["T"])*log2(v[clase]/v["T"]) 

            i+=1
    I = {}
    i = 0
    
    for key,values in columns.items():
        I[key] = [0.0,0.0] 
        for v in values.values():
            I[key][0] = I[key][0] + (v["T"]/datos)*v["E"]
        I[key][1] = p["E"]-I[key][0]
    
    print(I)
    return I

def main():
    data = get_data("arritmia.data")
    entropy(data)
    #Se van eliminando columnas cada ves que se selecciona una.

    training = data[:ceil(len(data)*0.75)]
    review = data[ceil(len(data)*0.75):]
main()