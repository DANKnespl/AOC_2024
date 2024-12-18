from collections import deque
from operator import itemgetter
import re
def load_data(size):
    f = open("inputs/day18.txt")
    coords = f.read().split("\n")
    f.close()
    start = (0,0)
    end = (size,size)
    for i,coord in enumerate(coords):
        data = re.findall(r"\d+",coord)
        if len(data)==0:
            coords.pop(i)
            break
        coords[i] = (int(data[0]),int(data[1]))
    walls = set()
    for x in range(-1,size+2):
        for y in range(-1,size+2):
            if x == -1 or x==size+1:
                walls.add((x,y))
            if y == -1 or y==size+1:
                walls.add((x,y))
    walls = list(walls)
    return coords, start, end, walls




def find_path(start, end, initial_direction, walls):
    queue = deque([(start, initial_direction, 0, [])])
    offset = 0
    minimum = float("inf")
    min_cost = {start: float("inf"),end:float("inf")}
    valid_sequnces = set()
    while queue:
        wonky = False    
        position, direction, cost, sequence = queue.popleft()
        seq = sequence.copy()
        seq.append(position)

        if position == end:
            if position in min_cost and cost > min_cost[position]:
                continue
            if minimum > cost:
                minimum = min(minimum, cost)
                valid_sequnces = set()
                min_cost[position] = minimum
            valid_sequnces.update(seq)
            continue

        if position in walls:
            continue
        
        if position in min_cost and cost >= offset + min_cost[position]:
            continue
        if position in min_cost and cost > offset/2 + min_cost[position]:
            wonky = True
            
        min_cost[position] = cost

        match direction:
            case "E":
                if not wonky:
                    queue.append(((position[0], position[1] - 1), "N", cost + offset + 1, seq))
                    queue.append(((position[0], position[1] + 1), "S", cost + offset + 1, seq))
                queue.append(((position[0] + 1, position[1]), "E", cost + 1, seq))
            case "N":
                if not wonky:
                    queue.append(((position[0] + 1, position[1]), "E", cost + offset + 1, seq))
                    queue.append(((position[0] - 1, position[1]), "W", cost + offset + 1, seq))
                queue.append(((position[0], position[1] - 1), "N", cost + 1, seq))
            case "W":
                if not wonky:
                    queue.append(((position[0], position[1] - 1), "N", cost + offset + 1, seq))
                    queue.append(((position[0], position[1] + 1), "S", cost + offset + 1, seq))
                queue.append(((position[0] - 1, position[1]), "W", cost + 1, seq))
            case "S":
                if not wonky:
                    queue.append(((position[0] + 1, position[1]), "E", cost + offset + 1, seq))
                    queue.append(((position[0] - 1, position[1]), "W", cost + offset + 1, seq))
                queue.append(((position[0], position[1] + 1), "S", cost + 1, seq))
                
    return minimum, list(valid_sequnces)

def drop_bytes(bytes, walls, time):
    for i in range(time):
        walls.append(bytes[i])

    

if __name__=="__main__":
    future_walls, start, end, walls = load_data(70)
    drop_bytes(future_walls,walls, 1024)
    min_len,break_points = find_path(start,end,"E",walls)
    for i in range(1024,len(future_walls)):
        walls.append(future_walls[i])
        if future_walls[i] not in break_points:
            continue
        _,break_points = find_path(start,end,"E",walls)
        if(len(break_points)==0):
            print(min_len, future_walls[i])
            break
