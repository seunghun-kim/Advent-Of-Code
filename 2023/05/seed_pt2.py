from copy import deepcopy

# f = open("./2023/05/example.txt")
f = open("./2023/05/input.txt")
lines = f.readlines()
f.close()

class Range:
    def __init__(self, start, size):
        self.start = start
        self.stop = start + size - 1
        self.size = size
        
    def is_overlapped(self, another):
        return not (self.start > another.stop or self.stop < another.start)
    
    def to_string(self):
        return "{} ~ {}".format(self.start, self.stop)
    
    def shift(self, amount):
        self.start += amount
        self.stop += amount
        
    def intersection(self, another):
        # 5가지 경우의 수 가능
        # 1. another과 겹치지 않음 -> self 리턴
        # 2. self 전체가 another와 겹칩(another가 self보다 큼) -> self 리턴
        # 3. self의 앞부분 일부만 another와 겹칩 -> 
        # 4. self의 뒷부분 일부만 another와 겹칩 -> 
        # 5. self의 가운데 일부가 another와 겹침 -> 겹치는 영역 리턴

        if not self.is_overlapped(another):  # 경우의 수 1
            # print("겹치지 않음")
            return None
        elif (self.start >= another.start) and (self.stop <= another.stop):  # 경우의 수 2
            return deepcopy(self)
        elif self.start < another.start and self.stop > another.stop:  # 경우의 수 5 (가운데 겹침)
            # print("가운데 겹침")
            return deepcopy(another)
        elif self.start <= another.stop and self.stop > another.stop: # 경우의 수 3 (앞부분만 겹침)
            # print("앞부분만 겹칩")
            
            r1_size = another.stop - self.start + 1
            return Range(self.start, r1_size)
        elif self.start < another.start and self.stop >= another.start:  # 경우의 수 4 (뒷부분만 겹침)
            # print("뒷부분만 겹침")
        
            r1_size = another.start - self.start
            r2_size = self.size - r1_size
            return Range(another.start, r2_size)
        else:
            return None
    
    def relative_complement(self, another):
        result = []

        # 5가지 경우의 수 가능
        # 1. another과 겹치지 않음 -> self 리턴
        # 2. self 전체가 another와 겹칩(another가 self보다 큼) -> self 리턴
        # 3. self의 앞부분 일부만 another와 겹칩 -> 
        # 4. self의 뒷부분 일부만 another와 겹칩 -> 
        # 5. self의 가운데 일부가 another와 겹침 -> 3개의 Range 리턴

        if (not self.is_overlapped(another)):
            result.append(deepcopy(self))
        elif ((self.start >= another.start) and (self.stop <= another.stop)):
            return None
        elif self.start < another.start and self.stop > another.stop:  # 경우의 수 5 (가운데 겹침)
            # print("가운데 겹침")
            
            r1_size = another.start - self.start
            r3_size = self.stop - another.stop
            result.append(Range(self.start, r1_size))
            # result.append(deepcopy(another))
            result.append(Range(another.stop + 1, r3_size))
        elif self.start <= another.stop and self.stop > another.stop: # 경우의 수 3 (앞부분만 겹침)
            # print("앞부분만 겹칩")
            
            r1_size = another.stop - self.start + 1
            r2_size = self.size - r1_size
            # result.append(Range(self.start, r1_size))
            result.append(Range(another.stop + 1, r2_size))
        elif self.start < another.start and self.stop >= another.start:  # 경우의 수 4 (뒷부분만 겹침)
            # print("뒷부분만 겹침")
        
            r1_size = another.start - self.start
            r2_size = self.size - r1_size
            result.append(Range(self.start, r1_size))
            # result.append(Range(another.start, r2_size))
        return result

# Get seeds as a list of integers
def parse_seeds(lines):
    # seeds: 1st line
    splitted = [int(x) for x in lines[0].split(' ')[1:]]
    result = []
    for i in range(0, len(splitted), 2):
        result.append(Range(splitted[i], splitted[i + 1]))
    return result

map_keywords = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

def parse_maps(lines, map_keyword):
    found = False
    result = []
    for line in lines:
        # 1. Find map_keyword string. If found, continue
        if map_keyword in line:
            found = True
            continue
        
        # 2. After map_keyword found, convert following lines until empty line appears
        if found:
            if line == '\n':
                break
            else:
                result.append([int(x) for x in line.split(' ')])
    
    return result

result = {"seed": [], "soil": [], "fertilizer": [], "water": [], "light": [], "temperature": [], "humidity": [], "location": []}
result["seed"] = parse_seeds(lines)

for keyword in map_keywords:  # seed -> soil, soil -> fertilizer 단계별 실행
    print("--------" + keyword + "--------")
    src_name = keyword.split('-')[0]  # "seed-to-soil" -> "seed"
    dst_name = keyword.split('-')[-1]  # "seed-to-soil" -> "soil"
    
    map_src_ranges = []
    map_dst_ranges = []
    for single_map in parse_maps(lines, keyword):
        map_src_ranges.append(Range(single_map[1], single_map[2]))
        map_dst_ranges.append(Range(single_map[0], single_map[2]))
    
    for i, src_val in enumerate(result[src_name]):  # src_val은 Range
        print("{}, {}: {}".format(src_name, i, src_val.to_string()))
        remaining = [src_val]
        # map을 먼저 적용. 적용된 영역은 제거, 적용 후 남은 영역은 remaining
        for i in range(len(map_src_ranges)):
            try:
                for single_range in remaining:
                    if single_range.is_overlapped(map_src_ranges[i]):  # 겹치는 경우
                        intersection = single_range.intersection(map_src_ranges[i])  # 교집합을 구함
                        intersection.shift(map_dst_ranges[i].start - map_src_ranges[i].start)  # 교집합에 map을 적용 (dst - src만큼 이동)
                        result[dst_name].append(intersection)  # map이 적용된 교집합을 결과에 추가
                        
                        remaining = single_range.relative_complement(map_src_ranges[i])  # 남은 값은 remaining으로 복사. 이때 남은 값이 없으면 None이 들어가 다음 루프에 TypeError 발생
            except TypeError:
                break
            
        # map 적용 후 남은 영역은 그대로 복사
        if remaining != None:
            result[dst_name].extend(remaining)
            
    for i, dst_elem in enumerate(result[dst_name]):
        print("{} {}: {}".format(dst_name, i, dst_elem.to_string()))
tmp = []
for elem in result['location']:
    tmp.append(elem.start)
print(min(tmp))
print("Done")