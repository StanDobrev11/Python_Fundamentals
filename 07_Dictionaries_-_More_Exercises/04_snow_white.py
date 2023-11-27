class Dwarf:
    def __init__(self, name, color, physics):
        self.name = name
        self.color = color
        self.physics = physics
        self.color_count = 0


command = input()

dwarfs = []

while command != "Once upon a time":
    name, color, physics = command.split(' <:> ')
    physics = int(physics)
    current_dwarf = Dwarf(name, color, physics)
    is_updated = False
    for idx, dwarf in enumerate(dwarfs):
        if name == dwarf.plant_name and color == dwarf.color and physics > dwarf.physics:
            dwarfs[idx] = current_dwarf
            is_updated = True
            break
    if is_updated:
        command = input()
        continue
    dwarfs.append(current_dwarf)
    command = input()

colors = {}
for dwarf in dwarfs:
    if dwarf.color not in colors:
        colors[dwarf.color] = 1
    else:
        colors[dwarf.color] += 1

for dwarf in dwarfs:
    dwarf.color_count = colors[dwarf.color]

for dwarf in sorted(dwarfs, key=lambda x: (x.physics, x.color_count), reverse=True):
    print(f'({dwarf.color}) {dwarf.name} <-> {dwarf.physics}')
