print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

#process
BMI = weight / (height ** 2)

#output
print("Your BMI =", BMI)