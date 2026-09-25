# เขียนฟังก์ชัน ชื่อ calculate_sphere(radius):
# คำนวนหา ปริมาตร ของทรงกลม volumn = 4.0 / 3 * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางจอ
#ไม่ลืมที่จะเขียนโปรแกรมในส่วนของการทดสอบการใช้งาน
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result
 
print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()
 
# Example 2: Function returning multiple values
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference
 
print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")