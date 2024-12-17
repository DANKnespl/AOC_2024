from collections import defaultdict
from operator import itemgetter


def load_data():
    f = open("inputs/day12.txt")
    lines = f.read().strip().split()
    f.close()
    return lines


def find_areas(data):
    areas = {}
    width = len(data[0])
    height = len(data)
    used = []
    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            repeat = False
            area = []
            if letter not in areas.keys():
                areas[letter] = []
                area = [(x, y)]
                used.append((x, y))
                repeat = True
            elif (x, y) not in used and data[y][x] == letter:
                repeat = True
                area = [(x, y)]
                used.append((x, y))

            new_area = []
            while repeat:
                new_area = area.copy()
                for _, point in enumerate(area):
                    if point[0]+1 < width:
                        if letter == data[point[1]][point[0]+1]:
                            new_area.append((point[0]+1, point[1]))
                            used.append((point[0]+1, point[1]))
                    if point[1]+1 < height:
                        if letter == data[point[1]+1][point[0]]:
                            new_area.append((point[0], point[1]+1))
                            used.append((point[0], point[1]+1))
                    if point[0]-1 >= 0:
                        if letter == data[point[1]][point[0]-1]:
                            new_area.append((point[0]-1, point[1]))
                            used.append((point[0]-1, point[1]))
                    if point[1]-1 >= 0:
                        if letter == data[point[1]-1][point[0]]:
                            new_area.append((point[0], point[1]-1))
                            used.append((point[0], point[1]-1))
                new_area = list(set(new_area))
                if len(new_area) == len(area):
                    areas[letter].append(area)
                    repeat = False
                area = new_area.copy()

    return areas

def get_perimeters(areas):
    area_perimeter = []
    for key in areas.keys():
        key_areas = areas[key]
        for _, ar in enumerate(key_areas):
            perimeter_sum = 0
            for _, point in enumerate(ar):
                point_sum = 4
                if (point[0]-1, point[1]) in ar:
                    point_sum -= 1
                if (point[0], point[1]-1) in ar:
                    point_sum -= 1
                if (point[0]+1, point[1]) in ar:
                    point_sum -= 1
                if (point[0], point[1]+1) in ar:
                    point_sum -= 1
                perimeter_sum += point_sum
            area_perimeter.append([key, len(ar), perimeter_sum, find_sides(ar)])
    return area_perimeter

def find_sides(region):
    sides = {}
    for x, y in region:
        left = (x - 1, y)
        right = (x + 1, y)
        up = (x, y - 1)
        down = (x, y + 1)

        if left not in region:
            if (x, "L") not in sides:
                sides[(x, "L")] = []
            sides[(x, "L")].append((x, y))
        if right not in region:
            if (x, "R") not in sides:
                sides[(x, "R")] = []
            sides[(x, "R")].append((x, y))
        if up not in region:
            if (y, "U") not in sides:
                sides[(y, "U")] = []
            sides[(y, "U")].append((x, y))
        if down not in region:
            if (y, "D") not in sides:
                sides[(y, "D")] = []
            sides[(y, "D")].append((x, y))
    side_count = 0

    for side in sides.keys():
        line = sides[side]
        line.sort(key=itemgetter(0,1))
        
        previous = line[0]
        it = 1
        while it < len(line):
            if not ((line[it][0] - previous[0] == 0 and line[it][1] - previous[1] == 1) or (line[it][1] - previous[1] == 0 and line[it][0] - previous[0] == 1)):
                side_count+=1
            previous = line[it]
            it+=1
        side_count+=1
    return side_count

def pt1(area_perimeter):
    ap_sum = 0
    for _,ap in enumerate(area_perimeter):
        ap_sum+= ap[1]*ap[2]
    return ap_sum
def pt2(area_perimeter):
    ap_sum = 0
    for _,ap in enumerate(area_perimeter):
        ap_sum+= ap[1]*ap[3]
    return ap_sum

if __name__ == "__main__":
    data = load_data()
    areas = find_areas(data)
    area_perimeters = get_perimeters(areas)
    print(pt1(area_perimeters))
    print(pt2(area_perimeters))
