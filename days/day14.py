import math
import io
def load_data():
    f = open("inputs/day14.txt")
    guards = []
    while True:
        guard = f.readline().strip().split(" ")
        if guard==[""]:
            break
        guard[0] = guard[0][2:].split(",")
        guard[1] = guard[1][2:].split(",")
        guard[0] = (int(guard[0][0]), int(guard[0][1]))
        guard[1] = (int(guard[1][0]), int(guard[1][1]))
        guards.append(guard)
    f.close()
    return guards

def find_positions(guards, seconds, width, height):
    positions = []
    for g, guard in enumerate(guards):
        position = ((guard[0][0]+guard[1][0]*seconds)%width,(guard[0][1]+guard[1][1]*seconds)%height)
        positions.append(position)
    return positions

def enumerate_quadrants(positions, width, height):
    quadrants={0:0, 1:0, 2:0, 3:0}
    
    for p, pos in enumerate(positions):
        
        quadrant = -10
        if pos[0] > math.floor(width/2):
            quadrant = 1
        elif pos[0] < math.floor(width/2):
            quadrant = 0
        if pos[1] < math.floor(height/2):
            quadrant+=0
        elif pos[1] > math.floor(height/2): 
            quadrant+=2
        else:
            quadrant-=10
        if quadrant>=0:
            quadrants[quadrant]+=1
    return quadrants

def pt1(quads):
    mul = 1
    for q in quads.values():
        mul *= q
    return mul



def pt2(guards,width,height):

    seconds = 0 #29689
    positions= 0
    likelyhood = 0
    max_likelyhood = 0
    while True:
        likelyhood = 0
        positions = find_positions(guards,seconds,width,height)
        quadrants = enumerate_quadrants(positions,width,height)
        mul = pt1(quadrants)
        p_flag = False
        positions = list(set(positions))
        for _,point in enumerate(positions):
            left = (point[0] - 1, point[1])
            right = (point[0] + 1, point[1])
            up = (point[0], point[1] - 1)
            down = (point[0], point[1] + 1)
            if left in positions or right in positions or up in positions or down in positions:
                likelyhood+=1
                if likelyhood>max_likelyhood:
                    max_likelyhood = likelyhood
                    p_flag = True            
        if p_flag:
            print(seconds, likelyhood)
        if seconds > 29689:
            break
        seconds+=1
    
    print(quadrants)
    return seconds

def visualize(positions, width, height):
    string = ""
    y = 0
    while y < height:
        #string = ""
        x=0
        while x < width:
            for p,pos in enumerate(positions):
                if pos==(x,y):
                    string+="#"
                else:
                    string+=" "
            x+=1
        string+="\n"
        y+=1
    print(string)

if __name__=="__main__":
    guards = load_data()
    width = 101
    height = 103
    seconds = 100
    #print(guards)
    positions = find_positions(guards,seconds,width,height)
    #print(positions)
    quadrants = enumerate_quadrants(positions,width,height)
    
    pt1(quadrants)
    print(pt2(guards,width,height))
    print(quadrants)