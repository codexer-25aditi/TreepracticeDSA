class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def SearchINTREE(rootNode,Value):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        queue=[]
        queue.append(rootNode)
        while(len(queue)>0):
            root=queue.pop()
            if root.data==Value:
                return "Success"
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        return "Not present in tree"

bst=Tree("Drinks")
n1=Tree("Hot")
n2=Tree("Cold")
n11=Tree("Tea")
n12=Tree("Coffee")
bst.left=n1
bst.right=n2
n1.left=n11
n1.right=n12
print(SearchINTREE(bst,"Hot"))
print(SearchINTREE(bst,"Juice"))

