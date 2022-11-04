# Your program should print each number from 1 to 100
# When the number is divisible by 3 then instead of printing the number it should print "Fizz"
# When the number is divisible by 5 then instead of printing the number it should print "Buzz"
# When the number is divisible by both 3 and 5 then instead of printing the number it should print "FIzzBuzz"

for num in range(1, 101):
    if num % 3 ==0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

