class Node:
    def __init__(self, value):
        """
        A node in a binary search tree.
    
        :param value: The value stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        """
        A binary search tree.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary search tree.
        """
        # Students will implement this
        done = False
        
        if self.root == None:
            self.root = Node(value)
            done = True
        
        current_node = self.root
        
        
        
        while done == False:
        
            # Go left (less than)
            if value < current_node.value:
                
                # if node has no child
                if current_node.left == None:
                    current_node.left = Node(value)
                    done = True
                
                else:
                    current_node = current_node.left
                    
            else:
                 # if node has no child
                if current_node.right == None:
                    current_node.right = Node(value)
                    done = True
                else:
                    current_node = current_node.right
                
                
        

    def search(self, value):
        """
        Searches for a value in the binary search tree.
        Returns True if found, False otherwise.
        """
        # Students will implement this
        if self.root == None:
            self.root = Node(value)
            done = True
        
        current_node = self.root
        
        
        
        while done == False:
        
            # Go left (less than)
            if value < current_node.value:
                
                # if node has no child
                if current_node.left == None:
                    current_node.left = Node(value)
                    done = True
                
                else:
                    current_node = current_node.left
                    
            else:
                 # if node has no child
                if current_node.right == None:
                    current_node.right = Node(value)
                    done = True
                else:
                    current_node = current_node.right
        
    def display(self, node):
        alist = []
        if node.left != None:
            alist = [self.display(node.left)]
        print(node.value)
        print(alist)
        alist.append(node.value)
        print(alist)
        if node.right != None:
            alist.append(self.display(node.right))

    def inorder_traversal(self):
        """
        Returns a list of values from an in-order traversal of the tree.
        """
        # Students will implement this
        self.display(self.root)
    
    
myTree = Tree()
myTree.insert(100)

myTree.insert(20)
myTree.insert(10)
myTree.insert(200)
myTree.insert(150)
myTree.inorder_traversal()