def check_chairs_to_visitors(chair_visitors: list):  # return boolean
    if len(chair_visitors[0]) >= int(chair_visitors[1]):
        return True
    else:
        return False


def calculate_missing_chairs(chairs_visitors: list):
    return int(chairs_visitors[1]) - len(chairs_visitors[0])


def total_free_chairs(total_chairs: list, total_visitors: list):
    total_chairs = "".join(total_chairs)
    total_visitors = list(map(int, total_visitors))
    return len(total_chairs) - sum(total_visitors)


number_of_rooms = int(input())
has_enough_chairs = True
total_chairs = []
total_visitors = []
for room in range(1, number_of_rooms + 1):
    chairs_visitors = input()
    chairs_visitors = chairs_visitors.split()
    total_chairs.append(chairs_visitors[0])
    total_visitors.append(chairs_visitors[1])
    if not check_chairs_to_visitors(chairs_visitors):
        print(f"{calculate_missing_chairs(chairs_visitors)} more chairs needed in room {room}")
        has_enough_chairs = False

if has_enough_chairs:
    print(f"Game On, {total_free_chairs(total_chairs, total_visitors)} free chairs left")
