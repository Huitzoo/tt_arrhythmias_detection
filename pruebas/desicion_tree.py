
#Depends of the number of our classes, the values are one or two... 
#Sentence it's only the name of the row of the table
class Rule():
    sentence = ""
    values = []


class Node():
    probability = []
    rules = []
    
    def create_rules(self,rules):
        pass

class Tree():
    n_nodes = 0
    nodes = []

    start_tree()

    def start_tree(self):
        pass


    def create_node(self):
        raise NotImplementedError