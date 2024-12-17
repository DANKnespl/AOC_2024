
def load_data():
    f = open("inputs/day15.txt")
    tmp = ""
    grid = []
    while tmp != "" or grid == []:
        tmp = f.readline().strip()
        grid.append(tmp)
    grid.pop()
    sequence = ""
    tmp = ""
    while sequence == "" or tmp != "":
        tmp = f.readline().strip()
        sequence += tmp
    return grid, sequence
    #(1300000 - 1377483)





def get_positions(grid,pt2=False):
    robot = []
    boxes = []
    walls = []
    new_grid = []
    for y, line in enumerate(grid):
        new_ln=""
        for x, letter in enumerate(line):
            match letter:
                case "@":
                    new_ln+="@."
                case "#":
                    new_ln+="##"
                case "O":
                    new_ln+="[]"
                case ".":
                    new_ln+=".."
        new_grid.append(new_ln)
        print(new_ln)

    if not pt2:
        for y, line in enumerate(grid):
            for x, letter in enumerate(line):
                match letter:
                    case "@":
                        robot = [x, y]
                    case "#":
                        walls.append([x, y])
                    case "O":
                        boxes.append([x, y])
    else:
        for y, line in enumerate(new_grid):
            for x, letter in enumerate(line):
                match letter:
                    case "@":
                        robot = [x, y]
                    case "#":
                        walls.append([x, y])
                    case "[":
                        boxes.append([x, y])
    return robot, walls, boxes


def move(position, direction, boxes, walls):
    next_pos = []
    additive = ()
    match direction:
        # <>>^>v
        case "^":
            additive = (0, -1)
        case ">":
            additive = (1, 0)
        case "v":
            additive = (0, 1)
        case "<":
            additive = (-1, 0)
    next_pos = [position[0]+additive[0], position[1]+additive[1]]
    if next_pos in walls:
        return False
    elif next_pos in boxes:
        if move(next_pos, direction, boxes, walls):
            if position in boxes:
                p = boxes.index(position)
                boxes[p] = next_pos
        else:
            return False
    else:
        if position in boxes:
            p = boxes.index(position)
            boxes[p] = next_pos
    return True


def move_2(position, direction, boxes, walls, depth=1):
    def do_move(position, direction, boxes, walls):
        next_pos = []
        additive = ()
        match direction:
            case "^":
                additive = (0, -1)
                next_pos = [position[0]+additive[0], position[1]+additive[1]]
                next_pos2 = [position[0]+additive[0]-1, position[1]+additive[1]]
                next_pos3 = [position[0]+additive[0]+1, position[1]+additive[1]]
                
                if next_pos in boxes:
                    do_move(next_pos, direction,boxes,walls)
                if next_pos2 in boxes:
                    do_move(next_pos2, direction,boxes,walls)
                if position in boxes and next_pos3 in boxes:
                    do_move(next_pos3, direction,boxes,walls)
                    
            case "v":
                additive = (0, 1)
                next_pos = [position[0]+additive[0], position[1]+additive[1]]
                next_pos2 = [position[0]+additive[0]-1, position[1]+additive[1]]
                next_pos3 = [position[0]+additive[0]+1, position[1]+additive[1]]
                
                if next_pos in boxes:
                    do_move(next_pos, direction,boxes,walls)
                if next_pos2 in boxes:
                    do_move(next_pos2, direction,boxes,walls)
                if position in boxes and next_pos3 in boxes:
                    do_move(next_pos3, direction,boxes,walls)
                
        if position in boxes:
            p = boxes.index(position)
            boxes[p] = next_pos
        return True
    
    next_pos = []
    additive = ()
    match direction:
        case ">":
            additive = (1, 0)
            next_pos = [position[0]+additive[0], position[1]+additive[1]]
            if next_pos in walls:
                return False
            elif next_pos in boxes:
                next_pos = [next_pos[0]+1,next_pos[1]]
                if move_2(next_pos, direction, boxes, walls):
                    previous_pos = [next_pos[0]-1,next_pos[1]]
                    if previous_pos in boxes:
                            p = boxes.index(previous_pos)
                            boxes[p] = next_pos
                    return True
                return False
            else:
                if position in boxes:
                    p = boxes.index(position)
                    next_pos = [next_pos[0]+1,next_pos[1]]
                    boxes[p] = next_pos
                return True
        case "<":
            additive = (-1, 0)
            next_pos = [position[0]+additive[0], position[1]+additive[1]]
            if next_pos in walls:
                return False
            next_pos = [next_pos[0]-1,next_pos[1]]
            if next_pos in boxes:
                #next_pos = [next_pos[0]-1,next_pos[1]]
                if move_2(next_pos, direction, boxes, walls):
                    if position in boxes:
                            p = boxes.index(position)
                            next_pos = [next_pos[0]+1,next_pos[1]]
                            boxes[p] = next_pos
                    return True
                return False
                    
            else:
                if position in boxes:
                    p = boxes.index(position)
                    next_pos = [next_pos[0]+1,next_pos[1]]
                    boxes[p] = next_pos
                return True

        case "^":
            additive = (0, -1)
            next_pos = [position[0]+additive[0], position[1]+additive[1]]
            next_pos2 = [position[0]+additive[0]-1, position[1]+additive[1]]
            next_pos3 = [position[0]+additive[0]+1, position[1]+additive[1]]
            can_move = True
            if next_pos in walls:
                return False
            if next_pos in boxes:
                can_move = can_move and move_2(next_pos, direction,boxes,walls)
            if next_pos2 in boxes:
                can_move = can_move and move_2(next_pos2, direction,boxes,walls)
            if position in boxes and next_pos3 in boxes:
                can_move = can_move and move_2(next_pos3, direction,boxes,walls)
            elif position in boxes and next_pos3 in walls:
                can_move = False
            
            if depth == 0:
                if next_pos in boxes and can_move:
                    do_move(next_pos, direction,boxes,walls)
                if next_pos2 in boxes and can_move:
                    do_move(next_pos2, direction,boxes,walls)

            return can_move
        case "v":
            additive = (0, 1)
            next_pos = [position[0]+additive[0], position[1]+additive[1]]
            next_pos2 = [position[0]+additive[0]-1, position[1]+additive[1]]
            next_pos3 = [position[0]+additive[0]+1, position[1]+additive[1]]
            can_move = True
            if next_pos in walls:
                return False
            if next_pos in boxes:
                can_move = can_move and move_2(next_pos, direction,boxes,walls)
            if next_pos2 in boxes:
                can_move = can_move and move_2(next_pos2, direction,boxes,walls)
            if position in boxes and next_pos3 in boxes:
                can_move = can_move and move_2(next_pos3, direction,boxes,walls)
            elif position in boxes and next_pos3 in walls:
                can_move = False
            
            if depth == 0:
                if next_pos in boxes and can_move:
                    do_move(next_pos, direction,boxes,walls)
                if next_pos2 in boxes and can_move:
                    do_move(next_pos2, direction,boxes,walls)
            return can_move
            
def visualize(grid,robot, walls, boxes):
    new_grid = []
    for y, line in enumerate(grid):
        new_ln=""
        for x in range(len(line)*2):
            if [x,y] in walls:
                new_ln+="#"
            elif [x,y] in boxes:
                new_ln+="["
            elif [x-1,y] in boxes:
                new_ln+="]"
            elif [x,y] == robot:
                new_ln+="@"
            else:
                new_ln+="."
        new_grid.append(new_ln)
        print(new_ln)
    print()

def pt1(boxes):
    val = 0
    for _, box in enumerate(boxes):
        val += 100*box[1]+box[0]
    print(val)


if __name__ == "__main__":
    grid, sequence = load_data()
    pt2 = True
    robot, walls, boxes = get_positions(grid, pt2)
    print(len(boxes))
    print(robot)
    for inp in range(len(sequence)):
        outcome = None
        pushes = False

        match sequence[inp]:
            case "^":
                additive = (0, -1)
            case ">":
                additive = (1, 0)
            case "v":
                additive = (0, 1)
            case "<":
                additive = (-1, 0)
        if [robot[0]+additive[0], robot[1]+additive[1]] in boxes:
            pushes = True

        if pt2:
            outcome = move_2(robot, sequence[inp], boxes, walls,0)
        else:
             outcome = move(robot, sequence[inp], boxes, walls)
        if outcome:
            match sequence[inp]:
                case "^":
                    additive = (0, -1)
                case ">":
                    additive = (1, 0)
                case "v":
                    additive = (0, 1)
                case "<":
                    additive = (-1, 0)
            robot= [robot[0]+additive[0], robot[1]+additive[1]]
    pt1(boxes)
    visualize(grid,robot,walls,boxes)

    
