people_on_queue = int(input())
lift = input().split()
max_capacity = 4 * len(lift)

lift = list(map(int, lift))
current_capacity = sum(lift)
while people_on_queue > 0 and current_capacity < max_capacity:
    for wagon in range(len(lift)):
        if lift[wagon] != 0:
            if lift[wagon] + people_on_queue <= 4:
                lift[wagon] += people_on_queue
                people_on_queue = 0
                break
            else:
                people_on_queue += lift[wagon]
                lift[wagon] = 4
                people_on_queue -= lift[wagon]
        else:
            if people_on_queue >= 4:
                lift[wagon] = 4
                people_on_queue -= 4
            else:
                lift[wagon] = people_on_queue
                people_on_queue = 0
    current_capacity = sum(lift)

if current_capacity < max_capacity:
    print("The lift has empty spots!")

if people_on_queue > 0:
    print(f"There isn't enough space! {people_on_queue} people in a queue!")

print(*lift)
