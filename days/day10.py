
def load_input():
    f = open("inputs/day10.txt")
    data = f.read().strip().split()
    f.close()
    return data

def find_value(x,y,val, top_map):
    sum = []
    sum2 = []
    if val == "10":
        return [(x,y)],[(x,y)]
    if x>0 and top_map[y][x-1] == val:
        tmp = find_value(x-1,y,str(int(val)+1),top_map)
        sum.extend(tmp[0])
        sum2.extend(tmp[1])
    if x<len(top_map[0])-1 and top_map[y][x+1] == val:
        tmp = find_value(x+1,y,str(int(val)+1), top_map)
        sum.extend(tmp[0])
        sum2.extend(tmp[1])
    if y>0 and top_map[y-1][x] == val:
        tmp = find_value(x,y-1,str(int(val)+1), top_map)
        sum.extend(tmp[0])
        sum2.extend(tmp[1])    
    if y<len(top_map)-1 and top_map[y+1][x] == val:
        tmp = find_value(x,y+1,str(int(val)+1), top_map)
        sum.extend(tmp[0])
        sum2.extend(tmp[1])
        
    if val == "1":
        return len(set(sum)), len(sum)
    return sum, sum2

def find_trials(top_map):
    sum = 0
    sum2=0
    for y, line in enumerate(top_map):
        for x in range(len(line)):
            if line[x] == "0":
                tmp = find_value(x,y,"1",top_map)
                sum+= tmp[0]
                sum2+= tmp[1]
    return sum, sum2

if __name__=="__main__":
    print(find_trials(load_input()))