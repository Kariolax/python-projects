import math
import time


# -------[FUNCTIONS]-------


def shot_details(gravity_amount):
    angle = 0
    speed = 0
    while True:
        try:
            angle = float(input("Input shot angle: "))
            if angle > 90 or angle < 1:
                print("Wrong value (range: 1 - 360)")
                continue
            break
        except ValueError:
            print("Character must be a number!")
            continue

    while True:
        try:
            speed = int(input("Input speed value: "))
            if speed > 200 or speed < 10:
                print("Wrong value (range: 10 - 201)")
                continue
            break
        except ValueError:
            print("Character must be a number!")
            continue

    bullet_range_temp = (((speed ** 2) * (math.sin(2 * math.radians(angle)))) / gravity_amount)
    bullet_range_round = round(bullet_range_temp)
    bullet_range = abs(bullet_range_round)
    return bullet_range


def shot_info(bullet_range, target):
    time.sleep(0.5)
    print("[Info]\nBullet distance: ", bullet_range, "[m]")
    time.sleep(2)
    print(f"Your target's place is {target - bullet_range}[m] from bullet distance")
    print("-----------------------------------")


def animation():
    for i in range(1, 4):
        print(".", end='')
        time.sleep(0.4)
    print(".", end='')
    time.sleep(0.2)
    print("BOOM!")
    time.sleep(0.5)
