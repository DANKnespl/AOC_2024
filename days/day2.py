

def p1():
    f = open("input.txt")
    counter = 0
    counter2 = 0
    while True:
        line = f.readline()
        if line=="":
            break
        day = line.rstrip().split(" ")
        if list_check1(day):
            counter+=1
        if list_check2(day):
            counter2+=1
    return counter, counter2
        
            
            
def list_check1(day):
    ascending = False
    prev = 0
    for i,st in enumerate(day):
        st = int(st)
        if i == 0:
            prev = st
            continue
        if i == 1 and prev-st>0:
            ascending=True
        elif prev-st==0:
            return False
        if ascending:
            if prev-st > 3 or prev-st <=0:
                return False
        else:
            if st-prev > 3 or st-prev <= 0:
                return False
        prev = st
    return True
                

def list_check2(day:list):
    if not list_check1(day):
        for i,_ in enumerate(day):
            day2 = day.copy()
            del day2[i]
            if list_check1(day2):
                return True
        return False
    return True
        


if __name__=="__main__":
    print(p1())