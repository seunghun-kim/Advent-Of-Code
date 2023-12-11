from termcolor import colored
from enum import Enum

class Direction(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3

class Pipe:
    available_types = "|-LJ7F"
    pipe_type = None
    pos = None  # (x, y)
    
    available_directions = {
        '|': (Direction.NORTH, Direction.SOUTH),
        '-': (Direction.EAST, Direction.WEST),
        'L': (Direction.NORTH, Direction.EAST),
        'J': (Direction.NORTH, Direction.WEST),
        '7': (Direction.SOUTH, Direction.WEST),
        'F': (Direction.SOUTH, Direction.EAST)
    }
    
    def __init__(self, pos, pipe_type):
        """Initialize Pipe instance

        Args:
            pos (tuple): (x, y), x: column idx, y: row idx
            pipe_type (str): char describes type of the pipe

        Raises:
            Exception: _description_
        """
        if pipe_type not in self.available_types:
            raise Exception("Type is not available")
        self.pos = pos
        self.pipe_type = pipe_type
        
    def get_available_directions(self):
        return self.available_directions[self.pipe_type]
    
    def is_entry_from_pos_available(self, entering_from):
        """_summary_

        Args:
            entering_from (tuple): (x, y) current cursor position
        """
        
        entrance = None
        
        if self.pos[0] > entering_from[0]:
            entrance = Direction.WEST
        elif self.pos[0] < entering_from[0]:
            entrance = Direction.EAST
        elif self.pos[1] > entering_from[1]:
            entrance = Direction.NORTH
        elif self.pos[1] < entering_from[1]:
            entrance = Direction.SOUTH
        
        return entrance in self.get_available_directions()
    
    def get_next(self, prev_location_tuple):
        """Returns next available position

        Args:
            prev_location_tuple (tuple): (x, y) tuple. Cursor's previous position.
        """
        entrance = None
        exit = None
        
        if self.pos[0] > prev_location_tuple[0]:
            entrance = Direction.WEST
        elif self.pos[0] < prev_location_tuple[0]:
            entrance = Direction.EAST
        elif self.pos[1] > prev_location_tuple[1]:
            entrance = Direction.NORTH
        elif self.pos[1] < prev_location_tuple[1]:
            entrance = Direction.SOUTH
            
        available = list(self.get_available_directions())
        available.remove(entrance)
        exit = available[0]
        
        next_pos = list(self.pos)
        if exit == Direction.NORTH:
            next_pos[1] -= 1
        elif exit == Direction.SOUTH:
            next_pos[1] += 1
        elif exit == Direction.WEST:
            next_pos[0] -= 1
        elif exit == Direction.EAST:
            next_pos[0] += 1
            
        return tuple(next_pos)

def find_start_pos(maze):
    for y, line in enumerate(maze):
        for x, ch in enumerate(line):
            if ch == 'S':
                return (x, y)

def print_status(positions, maze):
    box_map = {'|': '│', '-': '─', 'L': '└', 'J': '┘', '7': '┐', 'F': '┌'}
    
    print('-' * len(maze[0]))
    for y, line in enumerate(maze):
        for x, ch in enumerate(line):
            ch = box_map.get(ch, ch)
            if (x, y) == positions[-1]:
                ch = colored(ch, 'yellow')
            elif (x, y) in positions:
                ch = colored(ch, 'green')
            print(ch, end='')
    print()

def move(positions, distance, maze):
    # print_status(positions, maze)
    
    current_pos = positions[-1]
    prev_pos = positions[-2]
    
    current_ch = maze[current_pos[1]][current_pos[0]]
    if current_ch == 'S':
        return distance

    try:
        current_pipe = Pipe(current_pos, current_ch)
    except:
        print("Erorr finding route")
        print(positions)
        return None
    else:
        if not current_pipe.is_entry_from_pos_available(prev_pos):
            print("Erorr finding route")
            print(positions)
            return None
        
        next_pos = current_pipe.get_next(prev_pos)
        positions.append(next_pos)
        return move(positions, distance + 1, maze)

maze = []
with open("./2023/10/input.txt") as f:
    maze = f.readlines()

start_pos = find_start_pos(maze)

# Start moving
trajectory = [start_pos]

next_move = []
next_move.append((start_pos[0] - 1, start_pos[1]))
next_move.append((start_pos[0] + 1, start_pos[1]))
next_move.append((start_pos[0], start_pos[1] - 1))
next_move.append((start_pos[0], start_pos[1] + 1))

finished = False
for next in next_move:
    trajectory = [start_pos, next]
    # distance = move(trajectory, 1, maze)
    
    distance = 1
    
    current_pos = trajectory[-1]
    prev_pos = trajectory[-2]
    current_ch = maze[current_pos[1]][current_pos[0]]
    
    while current_ch != 'S':
        current_pos = trajectory[-1]
        prev_pos = trajectory[-2]
        
        current_ch = maze[current_pos[1]][current_pos[0]]
        if current_ch == 'S':
            print("Loop Found")
            print_status(trajectory, maze)
            print(int(distance / 2))
            finished = True
            break
        
        try:
            current_pipe = Pipe(current_pos, current_ch)
        except:
            print("Error finding route - can't proceed")
            print(trajectory)
            break
        else:
            if not current_pipe.is_entry_from_pos_available(prev_pos):
                print("Error finding route - can't proceed, blocked")
                print(trajectory)
                break
            
            next_pos = current_pipe.get_next(prev_pos)
            trajectory.append(next_pos)
            distance += 1
    if finished:
        break
print("Done")