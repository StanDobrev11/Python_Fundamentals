# x = lambda a, b: b * (a + 10)
# print(x(5, 2))

# def myfunc(n):
#   return lambda a: a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))
#
# # x = lambda a: a * 2
# # print(x(11))
def print_grade(grade):
    if 2 <= grade < 3:
        print("Fail")
    elif 3.00 <= grade <= 3.49:
        print("Poor")
    elif 3.50 <= grade <= 4.49:
        print("Good")
    elif 4.50 <= grade <= 5.49:
        print("Very Good")
    elif 5.50 <= grade <= 6.00:
        print("Excellent")


grade = float(input())
print_grade(grade)
