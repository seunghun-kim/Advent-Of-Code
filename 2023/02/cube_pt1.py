f = open('./2023/02/input.txt', 'r')
lines = f.readlines()
f.close()

max_values = { 'red': 12, 'green': 13, 'blue': 14 }

sum = 0

for line in lines:
    game_id = int(line.split(':')[0].split(' ')[1])
    # print(game_id)
    game_possible = True
    for revealed in line.split(': ')[1].split('; '):
        for cube in revealed.split(', '):
            num = int(cube.split(' ')[0])
            color = cube.split(' ')[1].replace('\n', '')
            # print("num: {}, color: {}".format(num, color))
            if (max_values[color] < num):
                game_possible = False
                break
        if not game_possible:
            break
    if game_possible:
        sum += game_id
print(sum)