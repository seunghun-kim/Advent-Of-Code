from copy import deepcopy

lines = []
with open('./2023/09/input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    numbers = [[int(x) for x in line.split()]]  # numbers[0]'s diff = numbers[1], numbers[1]'s diff = numbers[2], ...
    
    while numbers[-1].count(0) != len(numbers[-1]):
        diffs = []
        for i in range(len(numbers[-1]) - 1):
            num_now = numbers[-1][i]
            num_next = numbers[-1][i + 1]
            diff = num_next - num_now
            diffs.append(diff)
        numbers.append(deepcopy(diffs))
    # print(numbers)
    
    # Find left-most history value
    history_value = 0
    for i in range(1, len(numbers)):
        numbers[-(i + 1)].insert(0, numbers[-(i + 1)][0] - numbers[-i][0])
    print(numbers)
    
    sum += numbers[0][0]
print(sum)