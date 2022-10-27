## BMI Calculator

# Instructions

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#
# **Warning** you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75

# Example Output
# 80 ÷ (1.75 x 1.75) =  26.122448979591837
# Whole number = 26

"""Code"""
print("Your health is important to us. Please answer the following questions below, and we will give you, your BMI!")
weight = int(input("What is your current weight in kg? "))
height = float(input("What is your length in meters? "))
bmi = int(weight / (height**2))
print("Your bmi is: " + str(bmi))
