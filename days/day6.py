
def load_data():
    f = open("inputs/day6.txt")
    place = f.read().splitlines()
    f.close()
    start_pos = None
    for y, pl in enumerate(place):
        for x, letter in enumerate(pl):
            if letter == "^":
                start_pos = (x, y)
                return place, start_pos
    return place, start_pos


def new_pos(pos, change):
    return (pos[0]+change[0], pos[1]+change[1])


def alter_places(place, start_pos, history):
    new_places = []
    new_place = ""
    for _, point in enumerate(history):
        if point != start_pos:
            pl = place[point[1]]
            new_pl = pl[:point[0]] + "#" + pl[point[0] + 1:]
            new_place = place.copy()
            new_place[point[1]] = new_pl
            new_places.append(new_place)

    return new_places


def move(place, start_pos):
    facing = "N"
    pos = start_pos
    pos_history = []
    n_history = []
    while (pos[0] != 0 and pos[1] != 0 and pos[1] != len(place)-1 and pos[0] != len(place[0])-1):
        pos_history.append(pos)
        match facing:
            case "N":
                if pos in n_history:
                    return pos_history, False
                if (place[pos[1]-1])[pos[0]] == "#":
                    facing = "E"
                    n_history.append(pos)
                else:
                    pos = new_pos(pos, (0, -1))
            case "E":
                if (place[pos[1]])[pos[0]+1] == "#":
                    facing = "S"
                else:
                    pos = new_pos(pos, (1, 0))
            case "S":
                if (place[pos[1]+1])[pos[0]] == "#":
                    facing = "W"
                else:
                    pos = new_pos(pos, (0, 1))
            case "W":
                if (place[pos[1]])[pos[0]-1] == "#":
                    facing = "N"
                else:
                    pos = new_pos(pos, (-1, 0))

    pos_history.append(pos)
    return pos_history, True


if __name__ == "__main__":
    place, start_pos = load_data()
    history = move(place, start_pos)
    print(len(set(history[0])))

    places = alter_places(place, start_pos, list(set(history[0])))
    obstruction_count = 0

    for _, pl in enumerate(places):
        if not move(pl, start_pos)[1]:
            obstruction_count += 1
    print(obstruction_count)
