import math

def load_data():
    f = open("inputs/day5.txt")
    nl = ""
    rules = []
    orders = []
    while(True):
        nl = f.readline().strip().split("|")
        if len(nl)!=2:
            break
        rules.append(nl)
    while(True):
        nl = f.readline().strip().split(",")
        if len(nl)==1:
            break
        orders.append(nl)
    
    return rules, orders

def is_ordered(rules:list,order:list):
    for _,val in enumerate(rules):
        try:
            if order.index(val[0]) > order.index(val[1]):
                return False
        except:
            continue
    return True

def fix_order(rules,order:list):
    new_order = order.copy()
    while(not is_ordered(rules,new_order)):
        for _,val in enumerate(rules):
            try:
                i1 = new_order.index(val[0])
                i2 = new_order.index(val[1])
                if  i1 >  i2:
                    tmp = new_order[i1]
                    new_order[i1]=new_order[i2]
                    new_order[i2]=tmp
            except:
                continue
    return new_order

def sums(rules,orders):
    sum_correct = 0
    sum_incorrect = 0
    for _,val in enumerate(orders):
        if is_ordered(rules, val):
            sum_correct += int(val[math.ceil(len(val)/2)-1])
        else:
            sum_incorrect += int(fix_order(rules,val)[math.ceil(len(val)/2)-1])
            #print(val)
            #print(fix_order(rules,val))
            #print("")
            
    return sum_correct,sum_incorrect

if __name__=="__main__":
    rules, orders = load_data()
    print(sums(rules,orders))