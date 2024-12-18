import re
import math


def load_data():
    f = open("inputs/day17.txt")
    data = f.read().split("\n")
    f.close()
    data[0] = int(re.search(r"\d+", data[0]).group())
    data[1] = int(re.search(r"\d+", data[1]).group())
    data[2] = int(re.search(r"\d+", data[2]).group())
    data.pop(3)
    data[3] = re.findall(r"\d+", data[3])
    for i, val in enumerate(data[3]):
        data[3][i] = int(val)
    data[4] = 0
    return data


def get_combo(state, operand):
    match operand:
        case 4:
            return state[0]
        case 5:
            return state[1]
        case 6:
            return state[2]
        case 7:
            return -100
        case _:
            return operand


def do_instruction(state):
    out = ""
    match state[3][state[4]]:
        case 0:  # DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2, get_combo(state, state[3][state[4]+1]))
            state[0] = int(math.floor(numerator/denominater))
        case 1:
            state[1] = state[1] ^ state[3][state[4]+1]
        case 2:
            state[1] = get_combo(state, state[3][state[4]+1]) % 8
        case 3:
            if state[0] != 0:
                state[4] = state[3][state[4]+1]
                return ""
        case 4:
            state[1] = state[1] ^ state[2]
        case 5:
            out = str(get_combo(state, state[3][state[4]+1]) % 8)
        case 6:  # DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2, get_combo(state, state[3][state[4]+1]))
            state[1] = int(math.floor(numerator/denominater))
        case 7:  # DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2, get_combo(state, state[3][state[4]+1]))
            state[2] = int(math.floor(numerator/denominater))
    state[4] += 2
    return out


def pt2(inp):
    # B % 8 = 2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
    # XOR(B, A)%8 => B  - B {0,1,2,3,4,5,6,7}
    # XOR(B, 5) => B        {5,4,7,6,1,0,3,2}
    # DIV(A, 2^B) => C
    # XOR(B, 6) => B        {3,2,1,0,7,6,5,4}
    # DIV(A, 8) => A
    # XOR(B, C) => B
    #
    #
    # OUT = MOD(XOR(XOR(XOR(MOD(XOR(B, A), 8 , 5), 6), C), 8)
    #
    data = inp.copy()
    string = ""
    pattern = ""
    for _, num in enumerate(data[3]):
        if pattern != "":
            pattern += ","
        pattern += str(num)
    tmp = [0, 0]
    intervals = []
    flag = False
    flag2 = False
    
    length = len(inp[3])
    intervals = [[pow(8,length-1),pow(8,length)-1]]
    iteration_counter = 0
    iteration = 10
    while string != pattern and iteration!=1:
        iteration = int(10000000000/pow(5,iteration_counter))
        if iteration == 0:
            iteration = 1
        intervalz = intervals.copy()
        intervals=[]
        it = (intervalz[0][0])
        it -= iteration
        value = str(inp[3][-1-iteration_counter])
        position = -1-2*iteration_counter
        while string != pattern:
            it += iteration
            flag2 = False
            if it > intervalz[-1][1]+1:
                if flag == True:
                    tmp[1] = it
                    flag = False
                    intervals.append(tmp)
                break
            for i, interval in enumerate(intervalz):
                if it <= interval[1] and it >= interval[0]:
                    flag2 = True
                    break
            if not flag2:
                for i, interval in enumerate(intervalz):
                    if it < interval[0]:
                        it = intervalz[i][0] - iteration
                        if flag == True:
                            tmp[1] = intervalz[i-1][1]
                            flag = False
                            intervals.append(tmp)
                        break
                continue
            string = ""
            data = inp.copy()
            data[0] = it
            while (data[4] < len(data[3])-1):
                out = do_instruction(data)
                if out != "":
                    if string != "":
                        string += ","
                    string += out
            print(it, string, iteration, iteration_counter)
            if (not flag and (string[position] == value)):
                tmp = tmp.copy()
                tmp[0] = it - iteration
                flag = True
                # break
            if (flag and not (string[position] == value)):
                tmp[1] = it
                flag = False
                intervals.append(tmp)

        iteration_counter+=1
        print(intervals)
        #input()
    return it


if __name__ == "__main__":
    data = load_data()
    string = ""
    it = pt2(data)
    while (data[4] < len(data[3])-1):
        out = do_instruction(data)
        # print(data)
        if out != "":
            if string != "":
                string += ","
            string += out
    print(string, it)
