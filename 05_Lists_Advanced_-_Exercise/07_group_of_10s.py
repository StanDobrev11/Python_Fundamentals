# def filter_to_boundary_list():
#     for element in sequence:
#         if int(element) <= boundary:
#             boundary_list.append(element)
#
#
# def remove_from_sequence():
#     for element in boundary_list:
#         if element in sequence:
#             sequence.remove(element)
#
#
# sequence = input()
# sequence = sequence.split(", ")
# boundary = 10
# while len(sequence) > 0:
#     boundary_list = []
#     filter_to_boundary_list()
#     remove_from_sequence()
#     print(f'Group of {boundary}\'s: [{", ".join(boundary_list)}]')
#     boundary += 10

sequence = input()
sequence = sequence.split(", ")
boundary = 10

while len(sequence) > 0:
    boundary_list = [element for element in sequence if int(element) <= boundary]
    sequence = list(filter(lambda x: int(x) > boundary, sequence))
    print(f'Group of {boundary}\'s: [{", ".join(boundary_list)}]')
    boundary += 10
