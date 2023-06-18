class TREE:
    def __init__(self,data,children=[]):
        self.data=data
        self.children =children
    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret=ret+child.__str__(level+1)
        return ret
    def addCHild(self,TreeNode):
        self.children.append(TreeNode)

tree=TREE("Drink",[])
cold=TREE("Cold",[])
hot=TREE("hot",[])
tea=TREE("tea",[])
coffee=TREE("coffee",[])
cola=TREE("cola",[])
blackcola=TREE("black",[])



tree.addCHild(cold)
tree.addCHild(hot)
hot.addCHild(tea)
hot.addCHild(coffee)
cold.addCHild(cola)
cola.addCHild(blackcola)


print(tree)
