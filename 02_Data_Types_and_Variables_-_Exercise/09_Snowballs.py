balls_count = int(input())

best_value = 0
best_time = 0
best_weight = 0
best_quality = 0
for each_ball in range(balls_count):
    weight_of_snowball = int(input())
    time_travel = int(input())
    ball_quality = int(input())

    ball_value = (weight_of_snowball / time_travel) ** ball_quality
    if ball_value > best_value:
        best_value = ball_value
        best_time = time_travel
        best_weight = weight_of_snowball
        best_quality = ball_quality

print(f"{best_weight} : {best_time} = {best_value:.0f} ({best_quality})")
