happiness = input()
happiness_factor = int(input())

happiness = list(map(int, happiness.split()))
employee_happiness = list(map(lambda x: x * happiness_factor, happiness))

# print(employee_happiness)
av_happiness = sum(employee_happiness) / len(employee_happiness)
# print(av_happiness)
happy_employees = list(filter(lambda y: y >= av_happiness, employee_happiness))
# print(happy_employees)

if len(happy_employees) / len(employee_happiness) >= 0.5:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!")
