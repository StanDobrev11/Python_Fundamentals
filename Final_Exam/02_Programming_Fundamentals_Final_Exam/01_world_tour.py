def add_stop(planned_route, idx, string):
    if idx in range(len(planned_route)):
        return planned_route[:idx] + string + planned_route[idx:]

    return planned_route


def remove_stop(planned_route, start_idx, end_idx):
    if start_idx in range(len(planned_route)) and end_idx in range(len(planned_route)):
        return planned_route[:start_idx] + planned_route[end_idx + 1:]

    return planned_route


def switch(planned_route, old_str, new_str):
    if old_str in planned_route:
        return planned_route.replace(old_str, new_str)

    return planned_route


planned_route = input()
command = input()

while command != 'Travel':
    command = command.split(':')

    if command[0] == 'Add Stop':
        idx = int(command[1])
        string = command[2]
        planned_route = add_stop(planned_route, idx, string)
    elif command[0] == 'Remove Stop':
        start_idx = int(command[1])
        end_idx = int(command[2])
        planned_route = remove_stop(planned_route, start_idx, end_idx)
    elif command[0] == 'Switch':
        old_str = command[1]
        new_str = command[2]
        planned_route = switch(planned_route, old_str, new_str)

    print(planned_route)
    command = input()

print(f"Ready for world tour! Planned stops: {planned_route}")
