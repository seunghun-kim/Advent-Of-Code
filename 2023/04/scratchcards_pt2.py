# f = open("./2023/04/example.txt")
f = open("./2023/04/input.txt")
lines = f.readlines()
f.close()

number_of_instances = dict()
for i in range(1, len(lines) + 1):
    number_of_instances[i] = 1

for line in lines:
    game, numbers = line.strip().split(":")  # game = "Game 1", numbers = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    
    game_no = int(list(filter(None, game.split(" ")))[1])
    winning_numbers = [int(x) for x in numbers.split("|")[0].split()]
    numbers_i_have = [int(x) for x in numbers.split("|")[1].split()]
    
    match_count = 0
    for num in numbers_i_have:
        if num in winning_numbers:
            match_count += 1
    print("Game {} has {} matching cards".format(game_no, match_count))
        
    for i in range(game_no + 1, game_no + match_count + 1):
        try:
            number_of_instances[i] += number_of_instances[game_no]
            print("-> Game {} now has {} instances".format(i, number_of_instances[i]))
        except KeyError:
            break
    
# Sum of instances
sum = 0
for i in number_of_instances.values():
    sum += i
print("sum: " + str(sum))