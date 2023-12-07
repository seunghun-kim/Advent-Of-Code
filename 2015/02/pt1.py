lines = []
with open("./2015/02/input.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    w, h, l = [int(x) for x in line.split('x')]
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min([l*w, w*h, h*l])
    total = area + slack
    sum += total
print(sum)