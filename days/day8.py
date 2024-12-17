import math


def load_data():
    f = open("inputs/day8.txt")
    lines = f.read().split("\n")
    f.close()
    antenas = {}
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for x in range(len(line)):
            if line[x] == "." or line[x] == "\n" or line[x] == "":
                continue
            if line[x] in antenas:
                antenas[line[x]].append((x, y))
            else:
                antenas[line[x]] = [(x, y)]
    return antenas, width, height


def findAntis(antenas, dimensions):
    keys = list(antenas.keys())
    antis = []
    antis2 = []
    for _, key in enumerate(keys):
        positions = antenas[key]
        antis.extend(findPairs(positions, dimensions))
        antis2.extend(findPairs(positions,dimensions,True))
    print(len(list(set(antis))))
    print(len(list(set(antis2))))


    string = ""
    for y in range(dimensions[1]):
        for x in range(dimensions[0]):
            if (x,y) in antis2:
                string+="#"
            else:
                string+="."
        string+="\n"
    print(string)


def findPairs(positions, dimensions, pt2=False):
    antis = []
    for i, _ in enumerate(positions):
        for j in range(i+1, len(positions)):
            tmp = (positions[i][0] - positions[j][0],
                   positions[i][1] - positions[j][1])
            if math.copysign(1, tmp[0]) == math.copysign(1, tmp[1]):
                tmp = (abs(tmp[0]), abs(tmp[1]))
            mod1 = True
            mod2 = True
            cnt = 0
            if pt2:
                cnt = -1
            if (tmp[1] > 0):
                while (mod1):
                    cnt += 1
                    antis.append(
                        (positions[i][0]-tmp[0]*cnt, positions[i][1]-tmp[1]*cnt))
                    if antis[-1][0] < 0 or antis[-1][1] < 0:
                        antis.pop()
                        mod1 = False
                    if not pt2:
                        mod1= False
                cnt = 0
                if pt2:
                    cnt = -1
                while (mod2):
                    cnt += 1
                    
                    antis.append(
                        (positions[j][0]+tmp[0]*cnt, positions[j][1]+tmp[1]*cnt))
                    if antis[-1][0] >= dimensions[0] or antis[-1][1] >= dimensions[1]:
                        antis.pop()
                        mod2 = False
                    if not pt2:
                        mod2= False
            else:
                while (mod1):
                    cnt += 1
                    antis.append((positions[i][0]+tmp[0]*cnt, positions[i][1]+tmp[1]*cnt))
                    if antis[-1][0] >= dimensions[0] or antis[-1][1] < 0:
                        antis.pop()
                        mod1=False
                    if not pt2:
                        mod1= False
                cnt = 0
                if pt2:
                    cnt = -1
                while (mod2):
                    cnt += 1
                    antis.append((positions[j][0]-tmp[0]*cnt, positions[j][1]-tmp[1]*cnt))
                    if antis[-1][0] < 0 or antis[-1][1] >= dimensions[1]:
                        antis.pop()
                        mod2 = False
                    if not pt2:
                        mod2= False

    return antis



if __name__ == "__main__":
    antenas, width, heigth = load_data()
    dimensions = (width, heigth)
    findAntis(antenas, dimensions)
    
