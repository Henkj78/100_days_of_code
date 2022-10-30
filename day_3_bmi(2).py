print("Your health is important to us. Please answer the following questions below, and we will give you, your BMI!")
weight = int(input("What is your current weight in kg? "))
height = float(input("What is your length in meters? "))
bmi = round(weight / (height**2), 2)

if bmi < 18.5:
    print(f"Your BMI: {bmi}. You are underweight!")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI: {bmi}. You have a normal weight!")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI: {bmi}. You are overweight. Watch your diet!")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI: {bmi}. You are obese. Watch your diet and start walking for an hour a day!")
else:
    print("You are clinical obese. Please see a medic!")

