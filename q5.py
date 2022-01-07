from random import randint

MAX_FLOORS = 100
HIGHEST_FLOOR = randint(2, 100)
EGG_QTD = 2

print(f"****The highest floor: {HIGHEST_FLOOR}****")

eggs = EGG_QTD
floor_attempt = 2
count = 1
tries = 0
while eggs>0:
    tries += 1
    floor_attempt *= 2

    if floor_attempt > HIGHEST_FLOOR:
        eggs -= 1
        print(f"Egg break! You have {eggs} egg")
        floor_attempt = int(floor_attempt / 2 + 1)
        for i in range(floor_attempt, MAX_FLOORS):
            if i > HIGHEST_FLOOR:
                floor_attempt = i-1
                eggs -=1
                break
    else:
        print(f"Egg ok! You have {eggs} egg(s)")


print(floor_attempt)