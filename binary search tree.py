class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right = None
def insert_Node() :
    data= int (input ("enter the number:( Enter -1 for null|)"))

    if data == -1:
        return None
    node= Node(data)
    node.left =insert_Node()
    node.right =insert_Node()
    return node


def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder (node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')
def search(node, key):
    if node is None:
        return False

    if node.data == key:
        return True

    return search(node.left, key) or search(node.right, key)

root =None

while True :
    print ("1.insert_node\t2.preorder\t 3.inorder\t4.postorder \t 5.search\t 6.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        root=insert_Node()
    elif ch==2:
        print("preorder", end=' ')
        preorder(root)
        print()
    elif ch == 3:
        print("inorder", end=' ')
        inorder(root)
        print()
    elif ch == 4:
        print("postorder", end=' ')
        postorder(root)
        print()
    elif ch == 5:
        key = int(input("Enter the value to search: "))
        if search(root, key):
            print("Node found.")
        else:
            print("Node not found.")
    elif ch == 6:
        print("exit")
        break
    else:
        print("invalid choice")
