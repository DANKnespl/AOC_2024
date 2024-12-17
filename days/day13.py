import math
def load_data(pt2 = False):
    machines = []
    
    f = open("inputs/day13.txt")
    while True:
        button_A = f.readline().strip().split()[2:]
        if button_A == []:
            break
        button_B = f.readline().strip().split()[2:]
        prize = f.readline().strip().split()[1:]
        f.readline()
        button_A[0]= int(button_A[0][2:-1])
        button_A[1]= int(button_A[1][2:])
        button_B[0]= int(button_B[0][2:-1])
        button_B[1]= int(button_B[1][2:])
        prize[0]= int(prize[0][2:-1])
        prize[1]= int(prize[1][2:])
        if pt2:
            prize[0] += 10000000000000
            prize[1] += 10000000000000
        machines.append((button_A,button_B,prize))
    f.close()
    return machines

def solve_linear_equation(machine):
    X = 0
    Y = 1
    precision = 0.001   
    tmp = (-machine[1][X]/machine[0][X],machine[2][X]/machine[0][X]) #A
    y = (machine[2][Y]-machine[0][Y]*tmp[1])/(machine[1][Y]+machine[0][Y]*tmp[0])
    if abs(round(y)-y) > precision or round(y)<0:
        return None
    y = round(y)
    x = tmp[1]+ tmp[0]*y
    if abs(round(x)-x) > precision or round(x)<0:
        return None
    x = round(x)
    return(x,y)


if __name__=="__main__":
    machines = load_data(True)
    #m = [(2,4),(3,9),(6,15)]
    sum = 0
    for _,m in enumerate(machines):
        solution = solve_linear_equation(m)
        print(solution)
        if solution != None:
            sum+= solution[0]*3
            sum+= solution[1]*1
    print(sum)
