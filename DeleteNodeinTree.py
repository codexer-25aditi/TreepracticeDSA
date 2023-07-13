#to delete a node in binary tree:
#1.find the deepmost node in the tree
#2.replace the node to be deleted with deepmost node
#3.delete the end node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def deleteDeepestNode(root,deep):
    queue = []
    queue.append(root)
    while (len(queue) > 0):
        Node = queue.pop(0)
        if Node is deep:
            Node = None
            return "Deleted"

        if Node.left is deep:
            Node.left = None
            return "DEl"
        else:
            queue.append(Node.left)
        if Node.right is deep:
            Node.right = None
            return "Del"
        else:
            queue.append(Node.right)


#funct to delete an element in binary tree

def deleTE(key,root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        if root.data==key:
            return None
        else:
            return root
    key_node=None
    queue=[]
    queue.append(root)
    temp=None
    while(len(queue)>0):
        temp=queue.pop(0)
        if temp.data==key:
            key_node=temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    if key_node:
        x=temp.data
        deleteDeepestNode(root,temp)
        key_node.data=x
    return root



root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
print("The tree before deletion:")
inorder(root)
key=int(input())
root=deleTE(key,root)
print()
print("The tree after deletion:")
inorder(root)




