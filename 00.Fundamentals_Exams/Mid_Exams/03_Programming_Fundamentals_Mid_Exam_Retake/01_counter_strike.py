initial_energy = int(input())

battles_won = 0
total_battles = 0
is_finished = False
command = input()
while not command == 'End of battle':
    distance_to_enemy = int(command)
    total_battles += 1
    if initial_energy >= distance_to_enemy:
        initial_energy -= distance_to_enemy
        battles_won += 1
        if total_battles % 3 == 0:
            initial_energy += battles_won
    else:
        is_finished = True
        break
    command = input()
if is_finished:
    print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
else:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
