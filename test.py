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
            return False
        
        current_node = self.root
        
        while True:
        
            if value == current_node.value:
                return True
            # Go left (less than)
            if value < current_node.value:
                
                # if node has no child
                if current_node.left == None:
                    return False
                
                else:
                    current_node = current_node.left
                    
            else:
                 # if node has no child
                if current_node.right == None:
                    return False
                else:
                    current_node = current_node.right
        
    def display(self, node):
        alist = []
        if node.left != None:
            alist = self.display(node.left)

        alist.append(node.value)

        if node.right != None:
            alist += self.display(node.right)

        return alist

    def inorder_traversal(self):
        """
        Returns a list of values from an in-order traversal of the tree.
        """
        # Students will implement this
        return self.display(self.root)
    
    def del_node(self, value):

        done = False
        
        if self.root == None:
            return ('Tree is empty')
        
        current_node = self.root
        
        while done == False:

            if value == current_node.value:
                done = True
        
            # Go left (less than)
            elif value < current_node.value:
                
                # if node has no child
                if current_node.left == None:
                    return ('value has no node')
                
                else:
                    current_node = current_node.left
                    
            elif value > current_node.value:
                 # if node has no child
                if current_node.right == None:
                    return ('value has no node')
                
                else:
                    current_node = current_node.right
        #leaf node
        if current_node.left == None and current_node.right == None:
            print('hello')
            current_node = None
            print(current_node)
        #has child

        #has children
    
    
myTree = Tree()
myTree.insert(100)

myTree.insert(20)
myTree.insert(10)
myTree.insert(200)
myTree.insert(150)
myTree.insert(200)
myTree.insert(13)
myTree.insert(5600)
myTree.insert(1234)
myTree.insert(92)
myTree.insert(45)
myTree.insert(984)
myTree.insert(76)
myTree.del_node(13)
print(myTree.inorder_traversal())