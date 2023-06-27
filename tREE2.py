#Creation of binary tree using LL
class TreeNodes:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.RightChild=None


bsT=TreeNodes("Drinks")
left=TreeNodes("hot")
right=TreeNodes("Cold")
l1=TreeNodes("Coffee")
r1=TreeNodes("tea")
bsT.leftChild=left
bsT.RightChild=right
left.leftChild=l1
left.RightChild=r1
print("Preorder Traversal:")

def PreorderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    PreorderTraversal(rootnode.leftChild)
    PreorderTraversal(rootnode.RightChild)
PreorderTraversal(bsT)

print("Inorder Traversal:")
def InorderTraversal(rootnode):
    if not rootnode:
        return
    InorderTraversal(rootnode.leftChild)
    print(rootnode.data)
    InorderTraversal(rootnode.RightChild)

InorderTraversal(bsT)

print("PostOrder Traversal:")

def PostOrderTraversal(rootnode):
    if not rootnode:
        return
    PostOrderTraversal(rootnode.leftChild) #This kind of statement is always o(n/2)

    PostOrderTraversal(rootnode.RightChild)
    print(rootnode.data)

PostOrderTraversal(bsT)

def LevelOrderTraversal(rootnode):
    if not rootnode:
        return
    queue=[]
    queue.append(rootnode)

    while(len(queue)>0):
        print(queue[0].data,end=" ")
        node=queue.pop()
        if node.leftChild is not None:
            queue.append(node.leftChild)
        elif node.RightChild is not None:
            queue.append(node.RightChild)
print("LevelOrderTraversal:")

LevelOrderTraversal(bsT)