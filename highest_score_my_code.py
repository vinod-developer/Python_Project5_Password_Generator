# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max = student_scores[0]
length = len(student_scores)
for i in range(1, length):
    if max < student_scores[i]:
        max = student_scores[i]

print(f"The highest score in the class is: {max}")