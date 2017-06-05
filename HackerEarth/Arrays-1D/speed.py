T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    speed = map(int,raw_input().strip().split())
    cars = 0
    maxSpeed = 1000000000
    for k in range(N):
        if speed[k] <= maxSpeed:
            maxSpeed = speed[k]
            cars += 1

    print cars
