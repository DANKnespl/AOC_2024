def loadInput(input_file):
    list1 = []
    list2 = []
    f = open(input_file)
    while True:
        line = f.readline()
        if line == "":
            break
        values = line.strip().rsplit("   ")
        list1.append(int(values[0]))
        list2.append(int(values[1]))
    f.close()
    return list1,list2

def find_dif(l1,l2):
    dif = 0
    for i,val in enumerate(l1):
        dif+=abs(val-l2[i])    
    return dif

def find_sim(l1,l2):
    sim = 0
    for _,val in enumerate(l1):
        for _,val2 in enumerate(l2):
            if val==val2:
                sim+=val
    return sim

if __name__=="__main__":
    list1, list2 = loadInput("inputs/day1.txt")
    list1.sort()
    list2.sort()
    print(find_dif(list1,list2))
    print(find_sim(list1,list2))


