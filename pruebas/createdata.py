import random

with open("data.data","w") as data:
    for i in range(0,100):
        info = ""
        for j in range(0,10):
            info = info+str(random.randint(1,6))+","
        info = info + str(random.randint(1,3))+"\n"
        
        data.writelines(info)