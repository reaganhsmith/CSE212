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