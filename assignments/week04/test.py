#รับค่า ชื่อจริง จากผู้ใช้
#เขียน loop เพื่อนับจำนวน "สระที่มีอยู่ในชื่อที่รับมา" นั้นวาสมีจำนวนกี่ตัว
 
#ตัวอย่างอย่างหน้าจอ
 
#what is your name : Boonchoo
#Your name have 4 vowels.

name = input("what is your name?:")
vowels = 0

for letter in name:
    print(f"ตัวอักษร: {letter}")
    if letter == 'a' or letter == 'A':
        vowels = vowels + 1

    if letter == 'e':
        vowels = vowels + 1

print("Your name have", vowels, "vowels")
print("your name have {vowels} vowels")