# Input a Python list of student heights
# input()
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
hgt = 0
sum = 0
number_of_students = len(student_heights)
for hgt in range(0, number_of_students):
    sum += student_heights[hgt]

print(f"total height = {sum}")
print(f"number of students = {number_of_students}")
print(f"average height = {round(sum/number_of_students)}")