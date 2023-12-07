import math

lines = []
with open("./2023/06/example.txt") as f:
# with open("./2023/06/input.txt") as f:
    lines = f.readlines()
    
time = int(lines[0].replace(' ', '').split(':')[1])
goal = int(lines[1].replace(' ', '').split(':')[1]) + 1

x1 = (time - math.sqrt(time ** 2 - 4 * goal)) / 2
x2 = (time + math.sqrt(time ** 2 - 4 * goal)) / 2

button_min = math.ceil(x1)
button_max = math.floor(x2)

number_of_ways = button_max - button_min + 1
print(number_of_ways)