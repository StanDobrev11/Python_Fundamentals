key_line = input()
target_line = input()

key_line = key_line.split(', ')
target_line = target_line.split(', ')

key_result = [key for key in key_line for element in target_line if key in element]

final_result = [key for key in key_line if key in key_result]
print(final_result)
