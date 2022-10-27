# Create a program using maths and f-Strings that tells us how many days, weeks,
# months we have left if we live until 90 years old.

age = int(input("How old are you? "))
years_over = 90 - age

days = years_over * 365
weeks = years_over * 52
months = years_over * 12

print(f"If you want to finish off your bucketlist before you become 90, you have {months} months or {weeks} weeks "
      f"or {days} days left to do it!")
