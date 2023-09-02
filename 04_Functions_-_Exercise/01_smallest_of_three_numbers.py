def smallest_of_three(x, y, z):
    nums = [x, y, z]
    return min(nums)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest_of_three(num_1, num_2, num_3))
