# สามเหลี่ยม
def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * base * height
    print(f"Triangle with height {height} and width {base}")
    print(f"Area = 0.5 * {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5,7)
calculate_triangle_area(10,7)

# วงกลม
def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = 3.14 * radius * radius
    print(f"Circle with radius {radius}")
    print(f"Area = 3.14  × {radius}  × {radius} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5,7)
calculate_circle_area(10,7)
