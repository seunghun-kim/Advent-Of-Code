class Galaxy:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def distance(self, other):
        return abs((self.row - other.row)) + abs((self.col - other.col))


lines = []
with open('./2023/11/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
expandable_rows = list(range(len(lines)))
expandable_cols = list(range(len(lines[0])))
galaxies = []

for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch == '#':
            if row in expandable_rows: expandable_rows.remove(row)
            if col in expandable_cols: expandable_cols.remove(col)
            galaxies.append(Galaxy(row, col))

print(expandable_rows)
print(expandable_cols)

sum = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        pair = (galaxies[i], galaxies[j])
        dist = pair[0].distance(pair[1])
        
        for row in expandable_rows:
            if row > min(pair[0].row, pair[1].row) and row < max(pair[0].row, pair[1].row):
                dist += 1
        for col in expandable_cols:
            if col > min(pair[0].col, pair[1].col) and col < max(pair[0].col, pair[1].col):
                dist += 1
        
        # print(f"Pair {i}, {j}: distance = {dist}")
        sum += dist
        
print(sum)