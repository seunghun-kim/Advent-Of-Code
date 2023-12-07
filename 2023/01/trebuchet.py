import re

def find_classical():
    sum = 0
    with open("./2023/01/input.txt", "r") as f:
        lines = f.readlines()
        # Read line-by-line
        for line in lines:
            # Find first digit and last digit
            first, last = None, None
            for ch in line:
                if ch.isdecimal():
                    if first == None:
                        first = int(ch)
                    last = int(ch)
            
            # Combine two digits
            cal_val = first * 10 + last
            sum += cal_val
    print(sum)

def find_regex():
    sum = 0
    
    with open("./2023/01/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            cap = re.findall(r'(\d)', line)
            sum += int(cap[0] + cap[-1])
    print(sum)
    
def part2():
    spells = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sum = 0
    with open("./2023/01/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            first, last = None, None
            for i, ch in enumerate(line):
                if ch.isdecimal():
                    if first == None:
                        first = int(ch)
                    last = int(ch)
                else:
                    for num, spell in enumerate(spells):
                        if line[i:].startswith(spell):
                            if first == None:
                                first = num
                            last = num
            if line == "1six2twonecrb\n":
                print(line + ": " + str(first) + ", " + str(last))
            sum += first * 10 + last
    print(sum)

def part2_regex():
    dict_num = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    sum = 0
    with open("./2023/01/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            sum += int(dict_num.get(digits[0], digits[0]) + dict_num.get(digits[-1], digits[-1]))
    print(sum)

find_classical()
find_regex()
part2()
part2_regex()