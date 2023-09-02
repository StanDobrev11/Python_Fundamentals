def fire(mow: list, section: int, damage: int):
    """the pirate ship attacks the warship with the given damage at that section.
    Check if the index is valid and if not, skip the command.
    If the section breaks (health <= 0) the warship sinks,
        print the following and stop the program: "You won! The enemy ship has sunken."
"""
    is_broken = False
    if section in range(len(mow)):
        mow[section] -= damage
        if mow[section] <= 0:
            is_broken = True
    return mow, is_broken


def defend(ps: list, section_start: int, section_end: int, damage: int):
    """the warship attacks the pirate ship with the given damage at that range (indexes are inclusive).
     Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0)
     the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
"""
    is_broken = False
    if section_start in range(len(ps)) and section_end in range(len(ps)):
        for section in range(section_start, section_end + 1):
            ps[section] -= damage
            if ps[section] <= 0:
                is_broken = True
    return ps, is_broken

def repair(ps: list, section: int, health: int):
    """the crew repairs a section of the pirate ship with the given health.
     Check if the index is valid and if not, skip the command.
     The health of the section cannot exceed the maximum health capacity.
"""
    if section in range(len(ps)):
        if ps[section] + health > max_health_capacity:
            ps[section] = max_health_capacity
        else:
            ps[section] += health
    return ps

def status(ps):
    """prints the count of all sections of the pirate ship that need repair soon,
    which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
"""
    sections_to_repair = 0
    for section in ps:
        if section < max_health_capacity * 0.2:
            sections_to_repair += 1

    return sections_to_repair

pirate_ship = input()
pirate_ship = list(map(int, pirate_ship.split('>')))
man_o_war = input()
man_o_war = list(map(int, man_o_war.split('>')))
max_health_capacity = int(input())
mow_has_sunk = False
pirate_ship_has_sunk = False
command = input()
while command != 'Retire':
    command = command.split()
    if command[0] == 'Fire':
        index = int(command[1])
        value = int(command[2])
        man_o_war, mow_has_sunk = fire(man_o_war, index, value)
        if mow_has_sunk:
            break
    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        value = int(command[3])
        pirate_ship, pirate_ship_has_sunk = defend(pirate_ship, start_index, end_index, value)
        if pirate_ship_has_sunk:
            break
    elif command[0] == 'Repair':
        index = int(command[1])
        value = int(command[2])
        pirate_ship = repair(pirate_ship, index, value)
    elif command[0] == 'Status':
        damaged_sections_count = status(pirate_ship)
        print(f"{damaged_sections_count} sections need repair.")
    command = input()

if mow_has_sunk:
    print("You won! The enemy ship has sunken.")
elif pirate_ship_has_sunk:
    print("You lost! The pirate ship has sunken.")
else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(man_o_war)}")
