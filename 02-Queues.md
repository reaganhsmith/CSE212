# Data Structure: **QUEUES**

## Introduction: 
Have you ever stood in line at disney and then you see get people trying to get in front of you "to catch up with their group"? It can be very frustrating! Honestly waiting in lines in general is frustrating. Well with Python Queues the first in is also the first out. FIFO "First In, First Out." 

When you are in a line the person in the next in line to ride the rollercoaster is the **front**. The person at the end of the line is the **back**. Say the person in the front gets on the rollercoast and is no longer in line, they have now be **dequeued**. They ride the rollercoaster and then go to the back of the line. They are now the back and have been **enqueued**. 

From this example, it is apparent that queues can be used to process requests in an organized and orderly manner. No one gets to cut or jump ahead. The front gets dequeued when they leave and someone added to the back gets enqueued. 

## Read/Write a queue
When using Queues in python, they are represented using lists.
### Removing or DEQUEUE
A list has an idex of 0 at the first spot. Or the front. This means to dequeue (or remove) from the queue we would beed to get the item in the front at index[0] and then we could use delete or pop. 
Two examples of this would be:
front = my_queue[0]
```python
del my_queue[0]
```
This deletes the value at the front of the list. 

```python
**value = my_queue.pop(0)**
```
This one takes item at spot 0 (the front) and removes it from the list. 
It is like finally getting to ride the rollercoaster at Disney.

```python
my_fruits = ["apple", "banana", "kiwi", "strawberry", "mango"];
my_fruits.pop(0);
print(my_fruits)
```
The terminal will then print:
['apple', 'banana', 'kiwi', 'strawberry', 'mango']

### adding or ENQUEUE
To add to the queue all we need is to know the name of our list. We then can use append to add a value to the back of our queue. This is called **Enqueue**
An exmaple of this would be:
```python
my_queue.append(value)
```

```python
my_fruits = ["apple", "banana", "kiwi", "strawberry", "mango"];
my_fruits.append("grape");
print(my_fruits)
```
The terminal will then print:
['apple', 'banana', 'kiwi', 'strawberry', 'mango', 'grape']

This is saying add this value to the end of my list/queue. It is like getting in the back of the line for the rollercoaster.

### Other Queue Operations
We also might want to know the length of the queue. Its like being told at disney how many people are in front of you. To do this we can look at the length of our list. This looks like: 
```python
lengthOfQueue = len(my_queue)
```
Here is an example: 

```python 
my_queue = [1, 2, 3, 4, 5, 6];
length = len(my_queue);
print(length);
```
Then when we run this we get 6 printed in the terminal because there are 6 items in the queue. 


Another operation that might get used is empyty. This returns true if no one is in the queue. Like if the line at disney was empty it would say true. This is done by using an if statement and checking the length of the queue.
This would look like:
```python
if len(my_queue) == 0:
```

An example would be: 
```python
my_fruits = ["apple", "banana", "kiwi", "strawberry", "mango"];
if len(my_fruits) == 0 :
    print('true');
else:
    print('false');
```
This would print false because the list is not empty. 

# Problem to Solve: 



