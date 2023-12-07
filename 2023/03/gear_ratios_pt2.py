lines = []
# with open('./2023/03/example.txt') as f:
with open('./2023/03/input.txt') as f:
    lines = f.readlines()

class Number:
    __val = 0
    __row = 0
    __col_start = 0
    __col_end = 0
    
    def __init__(self, str_num, start):
        self.__row = start[0]
        self.__col_start = start[1]
        self.__col_end = start[1] + len(str_num) - 1
        self.__val = int(str_num)
    
    def is_adjacent(self, row, col):
        return row >= self.__row - 1 and row <= self.__row + 1 and col >= self.__col_start - 1 and col <= self.__col_end + 1
    
    def get(self):
        return self.__val


sum = 0
nums = []

for row, line in enumerate(lines):
    line = line.rstrip()
    
    num_buf = ""  # 숫자가 나타나는 경우, 연속된 숫자 문자열을 저장하는 변수
    is_num_valid = False  # 숫자가 유효한지 검사하는 플래그 (주변에 기호가 있는지)
    num_buf_start = ()
    
    for col, ch in enumerate(line):
        if ch.isdecimal():
            if num_buf == '':
                num_buf_start = (row, col)
            
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
                    nums.append(Number(num_buf, num_buf_start))
                    # print("{}({}, {}): Valid, sum = {}".format(num_buf, col, row, sum))
                else:
                    # print("{}({}, {}): Invalid, sum = {}".format(num_buf, col, row, sum))
                    pass
                num_buf = ""
                is_num_valid = False
                
for row, line in enumerate(lines):
    line = line.rstrip()
    for col, ch in enumerate(line):
        if ch == '*':
            print("* in ({}, {}) finding adjacent numbers".format(row, col))
            adj_nums = []
            for num in nums:
                if num.is_adjacent(row, col):
                    adj_nums.append(num)
                    print("adjacent number found: " + str(num.get()))
            if len(adj_nums) == 2:
                sum += adj_nums[0].get() * adj_nums[1].get()
                print("*({}, {}) is gear, ratio: {} * {} = {}".format(row, col, adj_nums[0].get(), adj_nums[1].get(), adj_nums[0].get() * adj_nums[1].get()))

print(sum)