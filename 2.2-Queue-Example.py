shopping_list = [];

# Add items to queue. remember first in, first out (FIFO) so we want to grab frozen ingredients last
shopping_list.append("Bread")
shopping_list.append("Crackers")
shopping_list.append("Peanutbutter")
shopping_list.append("Apples")
shopping_list.append("Broccoli")
shopping_list.append("Frozen Pizza")
shopping_list.append("Ice Cream")

print("")
# Lets view our list when we get to the store so we know what to buy:
for item in shopping_list:
    print(item)
print("")
# Then we will take our shopping list to the store and remove items from first to last while the list is not empty
while len(shopping_list) > 0:
    front_line = shopping_list[0]
    print('You picked up', front_line)
    shopping_list.pop(0)
    print(shopping_list)
    print("")
else:
    print("You have picked up everything off your list!")