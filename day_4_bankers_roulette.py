import random

names = input("Enter the names of everybody in the group: ")
names_in_list = names.split()
number_names = len(names_in_list)

random_name = random.randint(0, number_names - 1)
who_will_pay = names_in_list[random_name].capitalize()
print(f"The banker who is going to pay: {who_will_pay}")
