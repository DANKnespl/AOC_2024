import re
import math

def load_data():
    f = open("inputs/day17.txt")
    data = f.read().split("\n")
    f.close()
    data[0]=int(re.search(r"\d+",data[0]).group())
    data[1]=int(re.search(r"\d+",data[1]).group())
    data[2]=int(re.search(r"\d+",data[2]).group())
    data.pop(3)
    data[3]=re.findall(r"\d+",data[3])
    for i,val in enumerate(data[3]):
        data[3][i] = int(val)
    data[4]=0
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
        case 0: #DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2,get_combo(state, state[3][state[4]+1]))
            state[0] = int(math.floor(numerator/denominater))
        case 1:
            state[1] = state[1] ^ state[3][state[4]+1]
        case 2:
            state[1] = get_combo(state, state[3][state[4]+1])%8
        case 3:
            if state[0] !=0:
                state[4] = state[3][state[4]+1]
                return ""
        case 4:
            state[1] = state[1] ^ state[2]
        case 5:
            out = str(get_combo(state, state[3][state[4]+1])%8) 
        case 6: #DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2,get_combo(state, state[3][state[4]+1]))
            state[1] = int(math.floor(numerator/denominater))
        case 7: #DIV A/ 2^n
            numerator = state[0]
            denominater = pow(2,get_combo(state, state[3][state[4]+1]))
            state[2] = int(math.floor(numerator/denominater))
    state[4]+=2
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
    pattern=""
    for _,num in enumerate(data[3]):
        if pattern !="":
            pattern+=","
        pattern+=str(num)
    it = (105849472541256) #min 105883734377192
    #min answer = 105849372541256
    #max answer = 140737482541256
    tmp = [0,0]
    intervals = []
    flag = False
    flag2=False
    iteration = 10
    it -=iteration
    intervalz = [[105883734377256, 105883734381256], [105981155542256, 105981155574256], [105981155608256, 105981155640256], [105981155672256, 105981155738256], [105981156328256, 105981156360256], [105981156590256, 105981156624256], [105981156656256, 105981156688256], [105981156754256, 105981156786256], [106049875018256, 106049875052256], [106049875084256, 106049875116256], [106049875150256, 106049875216256], [106049875804256, 106049875838256], [106049876068256, 106049876100256], [106049876132256, 106049876166256], [106049876230256, 106049876264256], [106068577354256, 106068577356256], [106069202372256, 106069202404256], [106069202436256, 106069202470256], [106069202502256, 106069202568256], [106069203158256, 106069203190256], [106069203420256, 106069203452256], [106069203486256, 106069203518256], [106069203584256, 106069203616256], [106069248443256, 106069248451256], [106070260450256, 106070260482256], [106070260548256, 106070260582256], [108082757633256, 108082757641256], [108248898274256, 108248898306256], [108248898340256, 108248898372256], [108248898406256, 108248898470256], [108248899060256, 108248899094256], [108248899322256, 108248899356256], [108248899388256, 108248899420256], [108248899486256, 108248899520256], [108267600610256, 108267600616256], [108268225626256, 108268225660256], [108268225692256, 108268225726256], [108268225758256, 108268225824256], [108268226414256, 108268226446256], [108268226676256, 108268226708256], [108268226740256, 108268226774256], [108268226840256, 108268226872256], [108268271699256, 108268271701256], [108269283706256, 108269283738256], [108269283804256, 108269283836256], [109182269260256, 109182269266256], [109601812973256, 109601813005256], [109601813037256, 109601813071256], [109601813103256, 109601813169256], [109601813759256, 109601813791256], [109601814021256, 109601814053256], [109601814087256, 109601814119256], [109601814185256, 109601814217256], [110281780889256, 110281780891256], [110379202052256, 110379202086256], [110379202118256, 110379202152256], [110379202184256, 110379202250256], [110379202840256, 110379202872256], [110379203102256, 110379203134256], [110379203166256, 110379203200256], [110379203266256, 110379203298256], [110447921530256, 110447921562256], [110447921596256, 110447921628256], [110447921660256, 110447921726256], [110447922316256, 110447922348256], [110447922578256, 110447922610256], [110447922644256, 110447922676256], [110447922742256, 110447922774256], [110466623866256, 110466623866256], [110467248882256, 110467248916256], [110467248948256, 110467248980256], [110467249014256, 110467249080256], [110467249668256, 110467249702256], [110467249930256, 110467249964256], [110467249996256, 110467250030256], [110467250094256, 110467250128256], [110467294955256, 110467294961256], [110468306962256, 110468306994256], [110468307060256, 110468307092256]]
    while string!=pattern:
        it+=iteration
        flag2=False
        if it > 110468307092256+1:
            if flag== True:
                tmp[1]= it
                flag = False
                intervals.append(tmp)
            break
        for i, interval in enumerate(intervalz):
            if it <= interval[1] and it >= interval[0]:
                flag2=True
                break
        if not flag2:
            for i, interval in enumerate(intervalz):
                if it < interval[0]:
                    it=intervalz[i][0] - iteration
                    if flag== True:
                        tmp[1]= intervalz[i-1][1]
                        flag = False
                        intervals.append(tmp)
                    break                                   
            continue
        #it-=100000
        string=""
        data=inp.copy()
        data[0] = it
        while(data[4]< len(data[3])-1):
            out = do_instruction(data)
            if out != "":
                if string !="":
                    string+=","
                string+=out
        #if string[0]=="2":
        print(it, string)
        if (not flag and (string[-23]=="7")):
            tmp = tmp.copy()
            tmp[0]= it
            flag = True
            #break
        if (flag and not (string[-23]=="7")):
            tmp[1]= it
            flag = False
            intervals.append(tmp)
        
    print(intervals)
    return it

if __name__=="__main__":
    data = load_data()
    string = ""
    it = pt2(data)
    while(data[4]< len(data[3])-1):
        out = do_instruction(data)
        #print(data)
        if out != "":
            if string !="":
                string+=","
            string+=out
    print(string, it)
    