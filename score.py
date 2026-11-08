def score_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


students = [
    {"name": "Amy", "score": 88},
    {"name": "Ben", "score": 95},
    {"name": "Carmen", "score": 45},
    {"name": "David", "score":72},
]

total = 0
for s in students:
    level = score_level(s["score"]) 
    print(f"{s['name']}  {s['score']}  {level}")
    total = total + s["score"]

avg = total / len(students)
print(f"Average Scores: {avg:.1f}")

best = students[0]
for s in students:
    if s["score"] > best["score"]:
        best = s

print(f"The Highest Scores: {best['name']}  {best['score']}")
