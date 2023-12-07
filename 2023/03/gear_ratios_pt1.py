lines = []
# with open('./2023/03/example.txt') as f:
with open('./2023/03/input.txt') as f:
    lines = f.readlines()

sum = 0
count = 0

for row, line in enumerate(lines):
    line = line.rstrip()
    
    num_buf = ""  # 숫자가 나타나는 경우, 연속된 숫자 문자열을 저장하는 변수
    is_num_valid = False  # 숫자가 유효한지 검사하는 플래그 (주변에 기호가 있는지)
    
    for col, ch in enumerate(line):
        if ch.isdecimal():
            num_buf += ch
            
            # 주변 3x3 영역 내에 숫자, 온점이 아닌 다른 기호가 있는지 검사
            for y in range(row - 1, row + 2):
                for x in range(col - 1, col + 2):
                    # print("(x, y) = ({}, {})".format(x, y))
                    try:
                        if y == -1 or x == -1: raise IndexError
                        if (not lines[y][x].isdecimal()) and (lines[y][x] != '.') and (lines[y][x] != '\n'):
                            # print("Found symbol " + lines[y][x])
                            is_num_valid = True
                    except IndexError:
                        continue
        if (not ch.isdecimal()) or (col == len(line) - 1):
            if num_buf != "":
                if is_num_valid:
                    sum += int(num_buf)
                    count += 1
                    print("{}({}, {}): Valid, sum = {}".format(num_buf, col, row, sum))
                else:
                    print("{}({}, {}): Invalid, sum = {}".format(num_buf, col, row, sum))
                num_buf = ""
                is_num_valid = False

print(sum)
print(count)