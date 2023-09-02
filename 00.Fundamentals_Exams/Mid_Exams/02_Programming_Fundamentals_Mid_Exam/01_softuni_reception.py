import math

# employees helping students per hour
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

# every forth hour - break for an hour
max_students_assisted_per_hour = first_employee + second_employee + third_employee
time_needed_to_assist_all_students = math.ceil(students_count / max_students_assisted_per_hour)
rest_time = 0
if time_needed_to_assist_all_students > 3:
    rest_time = time_needed_to_assist_all_students // 3
    if time_needed_to_assist_all_students % 3 == 0:
      rest_time -= 1


time_needed_to_assist_all_students += rest_time

print(f"Time needed: {time_needed_to_assist_all_students}h.")