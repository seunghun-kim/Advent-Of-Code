f = open('./2023/02/input.txt', 'r')
lines = f.readlines()
f.close()


sum_of_power = 0

for line in lines:
    game_id = int(line.split(':')[0].split(' ')[1])
    cubes_minimum = { 'blue': 0, 'red': 0, 'green': 0 }
    
    for revealed in line.split(': ')[1].split('; '):
        for cube in revealed.split(', '):
            num = int(cube.split(' ')[0])
            color = cube.split(' ')[1].replace('\n', '')
            
            if (cubes_minimum[color] < num):
                cubes_minimum[color] = num
    
    power = cubes_minimum['blue'] * cubes_minimum['green'] * cubes_minimum['red']
    sum_of_power += power
            
print(sum_of_power)