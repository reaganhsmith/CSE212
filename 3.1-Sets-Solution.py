def find_repeat_ing(recipes):
    
    # Have aset to hold all the ingredients
    all_ingr = set()
    # Have another set to show the repeating ingredients
    repeat_ingr = set()
    
    # Look at each in the recipe so you can know if there is dduplicates
    for item in recipes:
        #Find out where the ingredients intersect and add that to our repeat set
        repeat_ingr.update(all_ingr.intersection(item))
        # Add all items to the all ingredients set
        all_ingr.update(item)
    
    # return our repeated list
    return repeat_ingr

# Function to combine our sets together.
def union_sets(recipe1, recipe2, recipe3):
    # create a new set to hold the combining of all the sets
    grocery_list = recipe1.union(recipe2, recipe3);
    # return this new grocoery list set
    return grocery_list;
    

# Function to check the leng of our new list
def count_items(set_name):
    # rturns the length
    return len(set_name)

# function to check if the item is in the set and if not add it. 
def add_to_groceries(item, set_name):
    # checks if the item is not in the list.
    if item not in set_name:
        # adds the item to your list.
        set_name.add(item)
    #returns the new list
    return set_name



# Tests to determine if everything is working

recipe1 = {"tomatoes", "onions", "garlic", "pasta", "steak"}
recipe2 = {"broccoli", "onions", "carrots", "chicken"}
recipe3 = {"pasta", "garlic", "olive oil", "carrots", "hamburger"}

# create an array holding all the sets to check for repeats
recipes = [recipe1, recipe2, recipe3]

print(" ")
duplicate_ingredients = find_repeat_ing(recipes)
print("Duplicate items:", duplicate_ingredients)
print(" ")

grocery_list = union_sets(recipe1, recipe2, recipe3)
print("Combined groceries:", grocery_list)
print(" ")

num_items = count_items(grocery_list)
print("Number of items to buy:", num_items)
print(" ")

# Adding last-minute items
grocery_list = add_to_groceries("broccoli", grocery_list) # Broccoli will not get added because it is already in the list
grocery_list = add_to_groceries("rice", grocery_list)

print("New list with added items:", grocery_list)
num_items = count_items(grocery_list)
print("New number of items:", num_items)
print(" ")