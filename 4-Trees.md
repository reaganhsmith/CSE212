# Data Structure: **TREES**
## Introduction
**Trees** are a collection of multiple nodes. They are non-linear data structures that are similar to linked lists. Trees connect to several different nodes. There are three types of trees: binary trees, binary search trees and balanced binary search trees. 
## Types of trees 
### Binary Trees
Binary Tree Data structures are a structure where each node has at max two children. The top node is called the root node and the two children are referred to as the left child and the right child. Nodes that are not connected to other nodes are leaf nodes. There will always be one root node. 
![Basic info on Binary Trees.](https://github.com/reaganhsmith/CSE212/blob/main/Binary_Tree.jpg)

### Binary Search Trees
**Binary Search Trees (BST)** are useful because they allow the user to keep a list of numbers that are sorted. It sorts and places data by comparing the data with the values of the parent nodes. Each node in this tree can have a max of 2 children nodes. Just like binary trees, these are called the left child and right child. The data less than the parent is placed to the left (left child) and the data that is greater than the parent node gets added to the right (right child). BST can find an element that is present in O(n) worst-case time. This means that when searching for an item in the BTS with worst-case scenario, it will take O(n) time. 

To add in the number 26:
- Compare 26 to the root node 20
- 26 > 20 so it goes to the right
- The compare 26 with the next node, 28
- 26 < 28 so it will go to the left
- 26 is now the left child of 28
![Basic info on Binary Search Trees.](https://github.com/reaganhsmith/CSE212/blob/main/BST.jpg)

### Balanced Binary Search Trees
**Balanced Binary Search Tree (balanced BST)** is the same as a BST except their is not a dramatic difference between the height of subtrees. The height is found by counting the number of nodes from the root. So in the image above ^^ 22 would have a height of 2 because it is two spots from the root (spot 20 and 15). Since 2 is not a dramatic difference, this tree is balanced.  There are a variety of different ways to check if a tree is balanced or unbalanced. Some algorithms are red black trees and AVL (Adelson-Velskii and Landis) trees. AVL can detect when the tree is unbalaced and perform a node rotation so that it becomes balanced. 
![Basic info on Balance BST](https://github.com/reaganhsmith/CSE212/blob/main/BalanceBST.jpg)
## Key terms
### Operations
To insert a value into a a BST use: insert(value)

To remove a value efrom a BST use: remove(value)

To check if a value is in the tree use: contains(value)

To view all values from smallest to largest use: traverse_forward

To view all values from largest to smallest use: traverse_reverse

To determine the height of a node in the tree use the root node and use: height(node)

To determine the size of the tree use: size()

To check if the tree is empty or not use (returns true or false): empty()
## Example
Here is an example of how trees are used, and values are inserted or removed. 
```python
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


```

# Problem to Solve
For work you are asked to create a Binary Search Tree that can add data, remove data and check if data is already in the tree. You are using a BST because you want the data to be ordered and you want to make sure no duplicate date gets inserted. For this to work properly do the following: 

1. Have a class to create the BST
2. Have a class to hold Node info
3. Initilize the date in your node class
4. Initilize the data in the BST class
5. Have a function to insert data
6. Have a function to follow the proper steps ot insert data (make sure to check if data is already in the tree)
7. Have a function to remove data from the tree
8. Have a function to check if the data is in the tree
9. Have funcntions to read and print the data from smallest to largest

**You can use the following scenario to test the program:** 
- Insert the data: 7,4,1,7,2,11
- Check if 1, 6, 10 and 11 are in the tree
- Remove 1 and 11 from the tree


Solution example [here](https://github.com/reaganhsmith/CSE212/blob/main/4.1-Trees-Solution.py)