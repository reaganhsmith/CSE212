class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(data, node.right)
        else:
            print(" ")
            print(f"{data} is already in the tree! {data} will not be inserted again.")
                 

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.data, end=' ')
            self._inorder_traversal(node.right)
    def print_tree(self):
        self._inorder_traversal(self.root)
        
    def _contains(self, data, node):
        if node is None:
            return False

        if data == node.data:
            return True
        elif data < node.data:
            return self._contains(data, node.left)
        else:
            return self._contains(data, node.right)
        
    def __contains__(self, data):
        return self._contains(data, self.root)
    
    def remove(self, data):
        self.root = self._remove(data, self.root)
        
    def _remove(self, data, node):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self._min_value_node(node.right).data
            
            node.right = self._remove(node.data, node.right)
            
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# TEST IT ALL!!!
# Create a tree using the BST class
new_tree = BST()
# add values to the tree!
new_tree.insert(7)
new_tree.insert(4)
new_tree.insert(1)
new_tree.insert(7)  # This will not be inserted as 7 already exists
new_tree.insert(2)
new_tree.insert(11)
print("")
# Print the tree
new_tree.print_tree()
print("\n")  # This will print a new line
print("---------------------------------------------")
print("Check if values are in tree. data 1, 6, 10:")

print(1 in new_tree) # True 
print(6 in new_tree) # False 
print(10 in new_tree) # False
print(11 in new_tree) # True

# Remove values 
print("---------------------------------------------")
print("Lets remove 1 and 11. Our new tree is:\n")
new_tree.remove(1)
new_tree.remove(11)

new_tree.print_tree()