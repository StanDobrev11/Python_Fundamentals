
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_material = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}

is_obtained = False
while not is_obtained:
    line = input().split()
    for idx in range(0, len(line), 2):
        quantity = int(line[idx])
        resource = line[idx + 1].lower()

        if resource in key_material:
            key_material[resource] += quantity
            if key_material[resource] >= 250:
                print(f'{legendary_items[resource]} obtained!')
                key_material[resource] -= 250
                is_obtained = True
                break

        elif resource not in junk_items:
            junk_items[resource] = quantity
        else:
            junk_items[resource] += quantity

for resource, quantity in key_material.items():
    print(f'{resource}: {quantity}')
for resource, quantity in junk_items.items():
    print(f'{resource}: {quantity}')


