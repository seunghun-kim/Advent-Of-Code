from termcolor import colored
from math import gcd

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

step = 0

current_nodes = []
node_steps = []

for node_name in nodes.keys():
    if node_name[-1] == 'A':
        current_nodes.append({'name': node_name, 'steps_took': 0})
remaining = len(current_nodes)

while remaining != 0:
    instruction = instructions[step % len(instructions)]
    # print(f"Step {step}")
    step += 1
    for i, node in enumerate(current_nodes):
        # print(f" - Node {i}, {node['name']} = ({colored(nodes[node['name']]['L'], 'green' if instruction == 'L' else 'red')}, {colored(nodes[node['name']]['R'], 'green' if instruction == 'R' else 'red')})")
        
        current_nodes[i]['name'] = nodes[node['name']][instruction]
        if current_nodes[i]['name'][-1] == 'Z':
            remaining -= 1
            current_nodes[i]['steps_took'] = step

print(current_nodes)

lcm = 1
for node in current_nodes:
    lcm = lcm * node['steps_took'] // gcd(lcm, node['steps_took'])
    
print(lcm)