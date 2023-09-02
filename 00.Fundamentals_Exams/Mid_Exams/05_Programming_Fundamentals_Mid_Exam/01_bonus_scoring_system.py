import math
import sys

number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())

max_attendance = 0
max_bonus = -sys.maxsize
for _ in range(number_of_students):
    student_attendance = int(input())
    if student_attendance > max_attendance:
        max_attendance = student_attendance
        max_bonus = (student_attendance / total_lectures) * (5 + additional_bonus)
    # total_bonus = (student_attendance / total_lectures) * (5 + additional_bonus)
    # if total_bonus > max_bonus:
    #     max_bonus = total_bonus
    #     max_attendance = student_attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.\n"
      f"The student has attended {max_attendance} lectures.")

