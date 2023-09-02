energy = 100
coins = 100

event_order = input()

event_order = event_order.split("|")
is_closed = False
for event in event_order:
    event = event.split("-")
    if event[0] == "rest":
        if energy <= 100 - int(event[1]):
            energy += int(event[1])
            print(f"You gained {event[1]} energy.")
        else:
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")
    elif event[0] == "order":
        energy -= 30
        if energy > 0:
            coins += int(event[1])
            print(f"You earned {event[1]} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= int(event[1]):
            coins -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event[0]}.")
            break

if not is_closed:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")
