import re

def load_input(path):
    f = open(path)
    string = f.read()
    f.close()
    return string


def mul(matches):
    sum = 0
    do = True
    for _,match in enumerate(matches):
        if do:
            if re.fullmatch(r"do\(\)",match) is not None:
                continue
            elif re.fullmatch(r"don\'t\(\)",match) is not None:
                do = False
                continue
            it = re.findall(r"\d{1,3}",match)
            sum += int(it[0])*int(it[1])
        elif re.fullmatch(r"do\(\)",match) is not None:
            do = True
            continue 
    return sum

if __name__=="__main__":
    string = load_input("inputs/day3.txt")
    l = re.findall(r"mul\(\d{1,3},\d{1,3}\)",string)
    k = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",string)
    print(mul(l))
    print(mul(k))
    