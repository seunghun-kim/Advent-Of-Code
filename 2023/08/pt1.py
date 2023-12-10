from termcolor import colored

instructions = ""
nodes = dict()


with open("./2023/08/input.txt", 'r') as f:
    lines = f.readlines()
    instructions = lines[0].strip()
    for line in lines[2:]:
        node_name = line.split()[0]
        next_l = line[7:10]
        next_r = line[12:15]
        nodes[node_name] = {'L': next_l, 'R': next_r}

print(instructions)
print(nodes)

step = 0
current_node = 'AAA'

while current_node != 'ZZZ':
    instruction = instructions[step % len(instructions)]
    
    print(f"Step {step}: {current_node} = ({colored(nodes[current_node]['L'], 'green' if instruction == 'L' else 'red')}, {colored(nodes[current_node]['R'], 'green' if instruction == 'R' else 'red')})")
    
    current_node = nodes[current_node][instruction]
    step += 1
    
print(step)