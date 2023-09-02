iterations = int(input())

positive_list = []
negative_list = []
count_positive = 0
sum_negative = 0
for each in range(iterations):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
        count_positive += 1
    else:
        negative_list.append(number)
        sum_negative += number

print(positive_list)
print(negative_list)
print("Count of positives:", count_positive)
print("Sum of negatives:", sum_negative)
