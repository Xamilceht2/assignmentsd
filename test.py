class Node:
    def __init__(self, value):
        """
        A node in a binary search tree.
    
        :param value: The value stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def del_node(self, value):
        if value < self.value:
            #has LC
            if self.left:
                self.left = self.left.del_node(value)

        if value > self.value:
            #has RC
            if self.right:
                self.right = self.right.del_node(value)

        else:
            if not self.right and not self.left:
                return None
            if not self.right:
                return self.left
            if not self.left:
                return self.right
        
        return self


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

    def delete(self, value):
        self.root.del_node(value)
        

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
myTree.delete(10)
print(myTree.inorder_traversal())