from random import randint

MAX_FLOORS = 100
HIGHEST_FLOOR = randint(2, 100)
HIGHEST_FLOOR = 33
EGG_QTD = 2

print(f"****The highest floor: {HIGHEST_FLOOR}****")

eggs = EGG_QTD
floor_attempt = 1
count = 1
tries = 0
while eggs>0:
    tries += 1
    floor_attempt += 10
    print(floor_attempt)
    if floor_attempt > HIGHEST_FLOOR:
        eggs -= 1
        print(f"Egg break! You have {eggs} egg")
        floor_attempt -=10 
        for i in range(floor_attempt, MAX_FLOORS):
            tries += 1
            print("I: ",i)
            if i > HIGHEST_FLOOR:
                floor_attempt = i-1
                eggs -=1
                break
    
    else:
        print(f"Egg ok! You have {eggs} egg(s)")





print(floor_attempt, tries)