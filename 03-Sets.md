# Data Structure: **SETS**
## Introduction 
Sets are useful in python data structure because they can store multiple things in a variable. Sets contain undordered, unchangable and unidexed collections. Like other things in python, sets do not worry about the order of the data. Order is not important in sets. 
Sets are written using curly brackets like this: 
```python
fruit_set = {"apples","mangos","pineapple"};
```
Because sets are unordered there is no sure way to know how the items will appear. 
Set items are unchangable. This means you cannot change items in the set. However you can add or remove items to it. 
Another thing about sets is that they do not allow duplicates. So for a set like: 
```python
fruit_set = {"apples","mangos","pineapple", "mangos"};
print(fruit_set);
```
When the set gets printed it will look like: {'apples','mangos','pineapple'}

Within a set, the values True and number 1 are considered the same and treated as a duplicate. False and 0 are also treated as duplicates. 
```python
fruit_set = {"apples","mangos","pineapple", True, 1, 2, 0, False};
print(fruit_set);
```
The results would look something like: {0, True, 2, 'pineapple', 'mangos', 'apples'}

## Hashing 
An important part of sets is called hashing. Hashing is used to achieve O(1) time when storeing data in a table. This allows for efficient adding, deleting and testing. 
Hashing is a data technique that takes date of random sizes and maps it to a fixed-size value. Hashing is done by detereming what index to put the data into. Like if ther was a list of numbers from 0-9 and we had an index ofo 0-9 we could get the index for the data by doing the following:
```python
 index(n) = n; # Where n is the number 0-9
```
We could also use this to determine the index of the number. This would look like: 
```python
n = index(n)
```
For more numbers and a small list we would use the modulo (%) operation to set the index of that number. We ccan use the following function: 
```python
index(n) = n % 10 # n is the number and 10 is the list size
```
A more general equation would be: 
```python
index(n) = hash(n) % list_size
```
hash(n) is a built-in python function that can convert non-itegers to a integer. These values change everytime the python script is ran but stays the same while running. Lists cannot be hashed. here is an example of hashing non-integers
```python
print(hash("cat")) # returns something like: 4592400767581790336
print(hash("Hello world")) # returns something like: -114912187815346267
print(hash(4.777)) #returns something like: 1791640018159040516
print(hash(False)) #Always returns a 0
print(hash(True)) #Always returns a 1
```
Hashing works well with sets because it checks if helps determine if that data is in theh set yet. When sets determine matching items they hash the value to the figure out if it is used in the set already. This makes it possible to check for values. 
Here is an example of that: 
```python
fruit_set = {"apples","mangos","pineapple"};

print("apples" in fruit_set); # Returns TRUE
print("kiwi" in fruit_set); # Returns FALSE
```
## Conflicts
Sometimes within hashing, 2 data items will be placed at the same index. Like if we wanted numbers 1-10 in a 5 spot list there 6 and 7 might both be placed at index 3. This is called a conflict. 
To deal with conflicts there are two possible solutions:
1. **Open Addressing** is the first option. 
2. 
## Key Methods

## Examples

