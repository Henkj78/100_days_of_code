# Can't use sum
# Can't use len

# make a list
student_heights = [167, 190, 201, 178, 185]

# Total height
total_height = 0
for height in student_heights:
    total_height += height
# test
# print(total_height)

# Average = total height / items in list
# Items in list
students = 0
for student in student_heights:
    students += 1
# test
# print(students)

# Average
average_height = round(total_height / students)
print(average_height)





