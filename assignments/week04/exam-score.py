scores = []

for i in range(1, 6):
    score = float(input(f"Enter score of student {i}: "))
    scores.append(score)

print()

for i in range(len(scores)):
    score = scores[i]
    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    
    formatted_score = int(score) if score.is_integer() else score
    print(f"Student {i+1}: {formatted_score} -> {result}")