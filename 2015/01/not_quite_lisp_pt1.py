with open("./2015/01_not_quite_lisp/input.txt") as f:
    line = f.readline()
    print(line.count('(') - line.count(')'))