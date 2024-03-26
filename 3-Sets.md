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
1. **Open Addressing** is the first option. open addressing can help us determine if something is already at that index. Then it will let us know to move it to the next open spot. This is usually done by moving the data to the right one index. This might cause more conflicts if other data is already in that index as well. 
2. **Chaining** is the second option. This option allows us to make a list to hold all the values that occupy that same space. This does not create more conflicts. 

To help with the preformance of our program, we might need to make the list holding the values bigger. This way there is less conflicts nad more places for data to go. 
## Key Methods

**Create Empty Set**
```python
my_fruit = set()
```
**Add to the Set**
```python
my_fruit = {"apples","mangos","pineapple"};
my_fruit.add("strawberries")
print(my_fruit) # Returns {'pineapple', 'mangos', 'Strawberries', 'apples'}
```

**Remove from the Set**
```python
my_fruit = {"apples","mangos","pineapple"};
my_fruit.add("strawberries")
my_fruit.remove("apples")
print(my_fruit) {'pineapple', 'strawberries', 'mangos'}
```

**Check if value in the set**
```python
fruit_set = {"apples","mangos","pineapple"};

print("apples" in fruit_set); # Returns TRUE
print("kiwi" in fruit_set); # Returns FALSE
```

**Size of the Set**
```python
fruit_set = {"apples","mangos","pineapple"};
len_set = len(fruit_set);
print(len_set); # Returns 3
```
**Intersection of TWO Sets**
we can find where two sets have matching points by determining where they intersect. This can be written in 2 ways:
1. 
```python

fruit_set = {"apples","mangos","pineapple"};
grocery_set = {"apples","chips","salsa","mangos"};

set3 = intersection(fruit_set, grocery_set);
print(set3); # Returns: {'mangos', 'apples'}
```
2. 
```python
fruit_set = {"apples","mangos","pineapple"};
grocery_set = {"apples","chips","salsa","mangos"};

set3 = fruit_set & grocery_set;
print(set3); # Returns: {'mangos', 'apples'}
```
The second method works better because nothing needs to be downloaded. 

**Union of TWO Sets**
We can also unite 2 different sets together. This is done in 2 ways: 
1. 
```python
fruit_set = {"apples","mangos","pineapple"};
grocery_set = {"apples","chips","salsa","mangos"};

set3 = union(fruit_set, grocery_set);
print(set3); # Returns: {'mangos', 'apples', 'salsa', 'pineapple', 'chips'}
```
2. 
```python
fruit_set = {"apples","mangos","pineapple"};
grocery_set = {"apples","chips","salsa","mangos"};

set3 = fruit_set | grocery_set;
print(set3);# Returns: {'mangos', 'apples', 'salsa', 'pineapple', 'chips'}
```
Again the second method works better because nothing needs to be downloaded. 

## Example
Here is an example of sets being used. 
```python
# Kate and Meg are turning 12 and planning their birthday part invite list
# Create 2 sets to store who visited these girls birthdays 
kate_birthday_set = {"Mary","Jack","Trish","Karen","Sylvia","Matt","Bob"};
meg_birthday_set = {"Litty","Poppy","Bob","Sylvia","Jane","Mark","Mat"};

# The birthday parties are on the same day at the same time!!!
# Use intersection to determine who cannot go to both parties. 
party_intersect = kate_birthday_set & meg_birthday_set;
print(party_intersect) # Bob and sylvia cannot attend both parties. 

# The girls realize they did this and decided to combine their party lists together:
party_union = kate_birthday_set | meg_birthday_set;
# Now everyone can come and eat yummy cake! Print a list of everyone who will be at the party
print(party_union);

# Kate and meg need to know how many people are attending to know how many party favors to make 
length_list = len(party_union);
print("There will be:" + str(length_list) + " kids in attendance")
```

# Problem to solve
Each week you go to meal prep recipes and determine what you need to get while grocery shopping. You get frustrated because some recipes have similar ingredients and you do not want to accidentally add them both to your list. You wish you could which ingredients repeat and then make sure they do not repeat in your final grocery list. You also wish you knew how many items where on your list so you could keep track of how many items are in your cart. This way you stick to your budget and don't go over. 

Write a group of functions to help you figure out what items are repeated for your recipes. Then combine all your recipes together to a single grocery list. Finally figure out how many items are in your list for while you shop. 

Last minute you remember a few things you want to add to your list! You want to check if it is already in your list and if not then you can add it in. 

Write a python program that: 
- Checks if ingredients are reepeated
- Combines all the recipes into a single set
- Counts how many items are in your new shopping set
- Adds an item to your shopping set if its not already in there 

**You can use the following scenario to test the program:** 
You found a few recipes you want to cook this week. the first is spicy chicken. It has the following ingredients:
1. Chicken 
2. Chili Paste
3. Broccoli
4. Carrots
The next recipe you want to make is chicken chili: 
1. Chicken 
2. Broth
3. Beans
4. Corn
The final recipe you want to make is steak bowls: 
1. Steak
2. Carrots
3. Broccoli
4. Corn
5. Onion
6. Quinoa

Solution example [here](https://github.com/reaganhsmith/CSE212/blob/main/3.1-Sets-Solution.py)