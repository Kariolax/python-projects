# Game - Tanks
# Your objective is simple - input angle value, then speed of bullet, and destroy your opponent.
# If bullet will explode on range of less than 5 meters next to your opponent - you win.
# Enjoy :)

# -------[Libraries]-------

import random
import time
from functions import shot_details, shot_info, animation

# -------[MAIN]-------
gravity = 9.81
hp = [1, 1]
player_name = []
turn = random.randrange(0, 2)
spot_1 = random.randrange(1, 1000)
spot_2 = spot_1 + random.randrange(200, 1000)
target = spot_2 - spot_1
player_name.append(input("Input name of first player : "))
player_name.append(input("Input name of second player : "))
print(f"{player_name[0]}'s spot: {spot_1}[m]")
print(f"{player_name[1]}'s spot: {spot_2}[m]")

while True:
    print(f"[Player: {player_name[turn]}]")
    bullet_range = shot_details(gravity)
    animation()
    shot_info(bullet_range, target)

    if bullet_range < target+5 and bullet_range > target-5:
        hp[turn] = 0
        print(f"You hit your opponent!")
        for i in range(1, 8):
            print(".", end='')
            time.sleep(0.3)
        print("")

    if hp[turn] == 0 or hp[turn-1] == 0:
        print(f"Congratulations {player_name[turn]}!\nYou won the match!")
        break

    if turn == 0:
        turn = 1
    else:
        turn = 0

print('GAME OVER')
