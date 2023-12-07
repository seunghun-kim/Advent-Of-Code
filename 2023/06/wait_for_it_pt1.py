import math

lines = []
with open("./2023/06/example.txt") as f:
# with open("./2023/06/input.txt") as f:
    lines = f.readlines()
    
times = [int(x) for x in list(filter(None, lines[0].split(' ')))[1:]]
distances = [int(x) for x in list(filter(None, lines[1].split(' ')))[1:]]

answer = 1
for i in range(len(times)):
    time = times[i]
    goal = distances[i] + 1
    
    x1 = (time - math.sqrt(time ** 2 - 4 * goal)) / 2
    x2 = (time + math.sqrt(time ** 2 - 4 * goal)) / 2
    
    button_min = math.ceil(x1)
    button_max = math.floor(x2)
    
    number_of_ways = button_max - button_min + 1
    
    answer = answer * number_of_ways
print(answer)