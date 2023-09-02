number_of_passengers = int(input())
elevator_capacity = int(input())

if number_of_passengers % elevator_capacity != 0:
    total_courses_needed = number_of_passengers // elevator_capacity + 1
else:
    total_courses_needed = number_of_passengers // elevator_capacity

print(total_courses_needed)
