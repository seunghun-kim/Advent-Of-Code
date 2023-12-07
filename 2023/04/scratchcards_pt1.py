# f = open("./2023/04/example.txt")
f = open("./2023/04/input.txt")
lines = f.readlines()
f.close()

total_points = 0

for line in lines:
    game, numbers = line.strip().split(":")  # game = "Game 1", numbers = "41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    winning_numbers = list(map(lambda x: int(x), filter(None, numbers.split("|")[0].split(" "))))
    numbers_i_have = list(map(lambda x: int(x), filter(None, numbers.split("|")[1].split(" "))))
    
    score = 0
    for num in numbers_i_have:
        if num in winning_numbers:
            score = score * 2 if score != 0 else 1
    
    total_points += score

print(total_points)