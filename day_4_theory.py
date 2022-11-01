"""Lists"""

# list is one of a few data structures = a way of organizing and storing data in Python.

# lists = store multiple items in a single variable in a ordered way.
# Lists = can have any (mixed) data types like: integers, floats, strings, lists, dictionaries e.d.
# lists = use [ ]

states = ["Delaware", "Pennsylvania", "Indiana", "Florida", "Washington" ]
# index =       0             1             2          3            4

print(states[0])  # output = Delaware
print(states[-1])  # output = last item Washington
last_item = states[-1]  # store last item in a new variable
print(last_item)

# change
states[1] = "Pencilvania"
print(states)

# add
states.append("Hawaii")  # adds item at end of the list
states.extend(["Arizona", "New Mexico"])  # extends the list

# Make list from string like input
names = input("Enter four names ")
names_list = names.split()  # separate names by space
print(names_list)

# OR

names = input("Enter four names, separated by a comma. ")
names_list = names.split(", ")  # separate by comma
print(names_list)

# Google for other list functions

# Nested lists

friends = ['geert', 'ruben', 'bart', 'jan peter']
colleagues = ['bas', 'roan', 'gert jan', 'michiel']

people = [friends, colleagues]
print(people)  # output is a nested list = list in list




