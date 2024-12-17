from collections import deque
from operator import itemgetter

def load_data():
    f = open("inputs/day16.txt")
    maze = f.read().split("\n")
    f.close()
    maze.pop()
    start = ()
    end = ()
    walls = []
    for y,line in enumerate(maze):
        for x,letter in enumerate(line):
            if letter == "S":
                start = (x,y)
            if letter == "E":
                end = (x,y)
            if letter == "#":
                walls.append((x,y))
    return maze, start, end, walls




def find_path(start, end, initial_direction, walls):
    queue = deque([(start, initial_direction, 0, [])])
    offset = 1000
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
        
        if position in min_cost and cost > 1000 + min_cost[position]:
            continue
        if position in min_cost and cost > 500 + min_cost[position]:
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



    

if __name__=="__main__":
    maze, start, end, walls = load_data()
    minimum, seqences = find_path(start,end,"E",walls)
    seqences.sort(key=lambda k: (-k[0], k[1]), reverse=True)
    print(minimum, len(seqences))