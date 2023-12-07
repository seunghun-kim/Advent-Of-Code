with open("./2015/01_not_quite_lisp/input.txt") as f:
    line = f.readline()
    floor = 0
    for i, ch in enumerate(line):
        if ch == '(': floor += 1
        elif ch == ')': floor -= 1
        if floor == -1:
            print(i + 1)
            break