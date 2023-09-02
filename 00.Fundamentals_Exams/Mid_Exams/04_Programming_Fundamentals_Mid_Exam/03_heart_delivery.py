def jump(lst, rng, psn):
    current_psn = psn + rng
    if current_psn >= len(lst):
        current_psn = 0

    if lst[current_psn] == 0:
        print(f"Place {current_psn} already had Valentine's day.")
    else:
        lst[current_psn] -= 2
        if lst[current_psn] == 0:
            print(f"Place {current_psn} has Valentine's day.")
    return lst, current_psn


houses_size = input()
houses_size = list(map(int, houses_size.split("@")))

cupid_psn = 0
command = input()
while not command == 'Love!':
    command = command.split()
    distance = int(command[1])
    houses_size, cupid_psn = jump(houses_size, distance, cupid_psn)

    command = input()

print(f"Cupid's last position was {cupid_psn}.")
is_valid = True
house_failed = 0
for house in houses_size:
    if house != 0:
        house_failed += 1
        is_valid = False

if is_valid:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_failed} places.")