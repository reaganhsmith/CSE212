class DMVLine:
    def __init__(self):
        # This creates the queue by creating a new list
        self.queue = []

    # This is the function to enqueue a person to the line!
    def enqueue(self, person):
        # Use APPEND to add a person to the front back of the line following (FIFO)
        self.queue.append(person)
        print(" ")
        print(f"{person} has been added to the line")

    def help_customer(self):
        # Runs an if statement to check of the queue is empty or not. 
        if len(self.queue) > 0:
             # If the queue is not empty it begins removing people as they get helped at the DMV
            helped_person = self.queue.pop(0)
            print(" ")
            print(f"{helped_person} has been helped with their DMV troubles")
             # Runs an if statement to check of the queue is empty or not. 
            if len(self.queue) > 0:
                # Gets the length of the queue so you know how many mroe people need ot be helped. 
                current_line_len = len(self.queue) 
                # While the queue is still not empty it tells you who is left inf the line
                print("Current line:", self.queue)
                print("There is", current_line_len, "people left")
            else:
                print("The line is gone! End of day!!")
        else:
            print("You helped everyone in the DMV. now you get to go home. YAY!!")



#Here is a test for the line
#this creates the new queue called dmv
dmv = DMVLine()

#These will add the names to the queue
dmv.enqueue("Susan")
dmv.enqueue("Cari")
dmv.enqueue("Bob")
dmv.enqueue("Jim")

# This runs while the dmv.queue exists. 
while dmv.queue:
    dmv.help_customer()