import random

attempts = 0
privat_num = random.randint(1, 100)

print("угадай число :)")

while True:
    our_num = int(input("введеное число: "))
    attempts += 1
    if our_num == privat_num:
        print("браво, число угаданно!!!")
        break

    elif our_num > privat_num:
        print("бери меньше")

    elif our_num < privat_num:
        print("бери больше")

print(f"кол-во попыток: {attempts}")