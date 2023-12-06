from itertools import groupby

with open("Day6/input.txt") as f:
    lines = f.read().splitlines()

aux = lines[0].split(" ")
times = []

# Part 1

for i in range(len(aux)):
    try:
        times.append(int(aux[i]))
    except:
        pass

aux = lines[1].split(" ")
distances = []
for i in range(len(aux)):
    try:
        distances.append(int(aux[i]))
    except:
        pass

def distance_traveled(vel, time):
    return vel * time

result = 1


for (time, distance) in zip(times, distances):
    temp = 0
    for i in range(time):
        if (distance_traveled(i, time-i) > distance):
            temp += 1
    result *= temp

print("Ex1: " + str(result))


# Part 2
        
new_times = ""
new_distances = ""

for time in times:
    new_times += str(time)

for distance in distances:
    new_distances += str(distance)

temp = 0
for i in range(int(new_times)):
    if (distance_traveled(i, int(new_times)-i) > int(new_distances)):
        temp += 1

print("Ex2: " + str(temp))