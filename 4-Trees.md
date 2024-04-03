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
```

# Problem to Solve