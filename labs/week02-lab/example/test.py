print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

# input
r = input("Radius: ")
r = float(r)

#process
area = 3.14159 * r ** 2
circumference = 2 * 3.14159 * r

#output
print("Area:", area)
print("Circumference: " + str(circumference))