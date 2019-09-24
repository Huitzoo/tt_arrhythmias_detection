def get_data_training(nombre):
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