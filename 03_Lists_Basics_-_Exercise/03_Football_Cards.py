string = input()

string = string.split()

team_a = []
team_b = []

for i in range(1, 12):
    player_a = "A-" + str(i)
    player_b = "B-" + str(i)
    team_a.append(player_a)
    team_b.append(player_b)

is_terminated = False
for i in range(len(string)):
    player_removed = string[i]
    if string[i] in team_a:
        team_a.remove(player_removed)
    elif string[i] in team_b:
        team_b.remove(player_removed)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")
