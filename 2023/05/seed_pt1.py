# f = open("./2023/05/example.txt")
f = open("./2023/05/input.txt")
lines = f.readlines()
f.close()

# Get seeds as a list of integers
def parse_seeds(lines):
    # seeds: 1st line
    return [int(x) for x in lines[0].split(' ')[1:]]

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

def solve_by_match_table():
    result = {"seed": parse_seeds(lines), "soil": [], "fertilizer": [], "water": [], "light": [], "temperature": [], "humidity": [], "location": []}

    for keyword in map_keywords:
        src_name = keyword.split('-')[0]  # "seed-to-soil" -> "seed"
        dst_name = keyword.split('-')[-1]  # "seed-to-soil" -> "soil"
        
        # Match table 만들기. map에 포함된 range 정보를 저장한다.
        match_table = {"src": [], "dst": []}
        for map_val in parse_maps(lines, keyword):
            dest_start= map_val[0]
            src_start = map_val[1]
            range_length = map_val[2]
            
            match_table["src"].extend(range(src_start, src_start + range_length))
            match_table["dst"].extend(range(dest_start, dest_start + range_length))
        
        # Match table을 기반으로 번호 매칭
        for src_val in result[src_name]:
            if src_val in match_table["src"]:
                result[dst_name].append(match_table["dst"][match_table["src"].index(src_val)])
            else:
                result[dst_name].append(src_val)

    print(result)
    print("Lowest location: " + str(min(result["location"])))
    

def solve_by_plus_operators():
    result = {"seed": parse_seeds(lines), "soil": [], "fertilizer": [], "water": [], "light": [], "temperature": [], "humidity": [], "location": []}
    
    for keyword in map_keywords:
        src_name = keyword.split('-')[0]  # "seed-to-soil" -> "seed"
        dst_name = keyword.split('-')[-1]  # "seed-to-soil" -> "soil"
        
        src_lst = result[src_name]
        for src_val in src_lst:
            dst_val = src_val
            
            for map_val in parse_maps(lines, keyword):
                map_src_start = map_val[1]
                map_src_end = map_val[1] + map_val[2]
                map_dst_start = map_val[0]
                
                if src_val >= map_src_start and src_val < map_src_end:
                    dst_val = map_dst_start + (src_val - map_src_start)
                    break

            result[dst_name].append(dst_val)
    print(result)
    print("Lowest location: " + str(min(result["location"])))

# solve_by_match_table()  # Match table 기반으로는 풀 수 없음 (리소스 사용량 과다)
solve_by_plus_operators()