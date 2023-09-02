start_value = ord(input())
end_value = ord(input())

target_string = input()

ttl_sum = 0
for ch in target_string:
    if ord(ch) in range(start_value + 1, end_value):
        ttl_sum += ord(ch)

print(ttl_sum)
