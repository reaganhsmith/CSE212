# Define a class to hold all the Binary Search Tree info
class BST:
    # Create another class to hold the nodes variables
    class Node:
        # Have a function to initilize the variables
        # give it parameters of self and data.
        def __init__(self, data):
            # define data
            self.data = data
            # define left and right child
            self.left = None
            self.right = None

    # exit Node class and create functions in BST class
    # function to initilze bst class
    def __init__(self):
        # create empty BST
        self.root = None

    # function to add data to the tree
    # Parameters of self and data
    def insert(self, data):
        # checks to see if the BST has a root or not
        if self.root is None:
            # If there is no root it sets it to the data from the nodes class
            self.root = self.Node(data)
        # if there is data it insert more data to that root
        else:
            # calls the insert function to add the data to the root.
            self._insert(data, self.root)  # Remember: data gets added starting at the root!!

    # we call a function on like 34 called _insert that we now need to create
    def _insert(self, data, node):
        # This function will help us properly add data to the tree
        # Check if the data is less than the data at that node
        if data < node.data:
            # if the data is less, it needs to go to the left
            # check if the left spot is empty or not
            if node.left is None:
                # if it is empty then add that data into that spot
                node.left = self.Node(data)
            # if that spot does have data in it then compare the data with the node data
            else:
                self._insert(data, node.left)
        # if the data > node.data than add it as the right child
        elif data > node.data:
            # This is similar to checking if the left exists but with the right side
            # and if not add it in. If it does exist the try inserting it to that node
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(data, node.right)
        # Finally, we will check if that value is already in the tree or not
        else:
            print(" ")
            print(f"{data} is already in the tree! {data} will not be inserted again.")

    # This function help print out the tree from small to large
    def _inorder_traversal(self, node):
        # checks if nodes exist and then if they do tells it how to print
        if node:
            self._inorder_traversal(node.left)
            print(node.data, end=' ')
            self._inorder_traversal(node.right)
    # function to used the order traversal to print the tree
    def print_tree(self):
        self._inorder_traversal(self.root)
        


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
print(" ")
# Print the tree
new_tree.print_tree()
print(" ")

