"""
สร้างไฟล์ใหม่ใน FOLDER /assignments/
week09/lab-assignment-1109.py

เครื่องคำนวณค่าไฟฟ้าแบบขั้นบันได
เขียนโปรแกรมคำนวณค่าไฟฟ้าจากจำนวนหน่วยไฟฟ้าที่ใช้ในเดือนนั้น โดยใช้ฟังก์ชัน
calculate_electricity_cost(units)

ค่าไฟฟ้าขึ้นกับปริมาณใช้งาน
จำนวนหน่วยที่ใช้     อัตราต่อหน่วย
1-50 หน่วยแรก       2.50 บาท
51-100 หน่วย        3.00 บาท
101-200 หน่วย       3.50 บาท
มากกว่า 200 หน่วย    4.00 บาท

ให้คิดค่าบริการคงที่เพิ่มอีก 25 บาทต่อเดือน
เงื่อนไข
- โปรแกรมแสดงเมนูวนซ้ำ
- ผู้ใช้เลือก 1 เพื่อคำนวณค่าไฟ
- ผู้ใช้เลือก 2 เพื่อออกจากโปรแกรม
- หากเลือกเมนูอื่น ให้แจ้งว่าเลือกเมนูไม่ถูกต้อง
- จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ
- ให้แสดงรายละเอียดค่าไฟแต่ละช่วง และยอดรวมสุทธิ

1-50 หน่วย: 125.00 บาท
51-100 หน่วย: 150.00 บาท
101-120 หน่วย: 70.00 บาท
ค่าบริการ: 25.00 บาท
รวมค่าไฟฟ้าทั้งสิ้น: 370.00 บาท
"""

def calculate_electricity_cost(units):
    if units < 0:
        print("Error: จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ!")
        return

    service_fee = 25.00
    

    if units > 200:
        cost_1_50 = 2.50 * 50
        cost_51_100 = 3.00 * 50
        cost_101_200 = 3.50 * 100
        cost_over_200 = 4.00 * (units - 200)
        total_cost = cost_1_50 + cost_51_100 + cost_101_200 + cost_over_200 + service_fee
        
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print("101-200 หน่วย: 350.00 บาท")
        print(f"201-{units} หน่วย: {cost_over_200:.2f} บาท")
        print(f"ค่าบริการ: {service_fee:.2f} บาท")
        print(f"รวมค่าไฟฟ้าทั้งสิ้น: {total_cost:.2f} บาท")

  
    elif units > 100:
        cost_1_50 = 2.50 * 50
        cost_51_100 = 3.00 * 50
        cost_101_200 = 3.50 * (units - 100)
        total_cost = cost_1_50 + cost_51_100 + cost_101_200 + service_fee
        
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print(f"101-{units} หน่วย: {cost_101_200:.2f} บาท")
        print(f"ค่าบริการ: {service_fee:.2f} บาท")
        print(f"รวมค่าไฟฟ้าทั้งสิ้น: {total_cost:.2f} บาท")


    elif units > 50:
        cost_1_50 = 2.50 * 50
        cost_51_100 = 3.00 * (units - 50)
        total_cost = cost_1_50 + cost_51_100 + service_fee
        
        print("1-50 หน่วย: 125.00 บาท")
        print(f"51-{units} หน่วย: {cost_51_100:.2f} บาท")
        print(f"ค่าบริการ: {service_fee:.2f} บาท")
        print(f"รวมค่าไฟฟ้าทั้งสิ้น: {total_cost:.2f} บาท")


    else:
        cost_1_50 = 2.50 * units
        total_cost = cost_1_50 + service_fee
        
        print(f"1-{units} หน่วย: {cost_1_50:.2f} บาท")
        print(f"ค่าบริการ: {service_fee:.2f} บาท")
        print(f"รวมค่าไฟฟ้าทั้งสิ้น: {total_cost:.2f} บาท")


while True:
    print("\n--- เครื่องคำนวณค่าไฟฟ้า ---")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")
    
    choice = input("เลือกเมนู (1 หรือ 2): ")
    
    if choice == '1':
        try:
            user_units = int(input("กรอกจำนวนหน่วยไฟฟ้า: "))
            calculate_electricity_cost(user_units)
        except ValueError:
            print("กรุณากรอกตัวเลขจำนวนเต็มเท่านั้น!")
    elif choice == '2':
        print("ออกจากโปรแกรมเรียบร้อยแล้ว")
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่อีกครั้ง")