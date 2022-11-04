# expect total of sum of all the even numbers

total = 0
# 1 to 100 --> you have to add one more (range is to not including)
for num in range(1, 101):
    if num % 2 == 0:
        total += num
print(total)
