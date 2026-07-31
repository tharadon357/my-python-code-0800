weight = float(input("Enter weight in kilograms (kg): "))
height = float(input("Enter height in meters (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI: {bmi:.1f}")

if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi <= 24.9:
    print("BMI Category: Normal weight")
elif bmi <= 29.9:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")