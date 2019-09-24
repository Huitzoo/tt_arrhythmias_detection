from math import ceil

def get_data():
    data_arritmia = []
    with open("arritmia.data","r") as data:
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


def get_data():
    data_arritmia = []
    with open("data.data","r") as data:
        data = data.readlines()
    i = 0
    for d in data:
        aux_data = []
        for fact in d.split(","):
            aux_data.append(float(fact))
        data[i] = aux_data
        i += 1
    return data
    
def main():
    #data is an array with 280 elements
    data = get_data()
    for d in data:
        if d[29] != 0.0:
            print(d[-1])
    training = data[:ceil(len(data)*0.75)]
    review = data[ceil(len(data)*0.75):]
main()