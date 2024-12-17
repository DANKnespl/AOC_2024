import re


def find_pattern(main):
    list_2d = []
    for i, val in enumerate(main):
        list_2d.append(list(val.strip()))
    return list_2d


def horizontal_solution(text, pattern):
    string = ""
    counter = 0
    for i, val in enumerate(text):
        string = ""
        for j, letter in enumerate(val):
            string += letter
            if len(string) == len(pattern):
                m = re.match(string, pattern)
                if m is not None:
                    counter += 1
                m = re.match(string, pattern[::-1])
                if m is not None:
                    counter += 1
                string = string[1:]
    return counter


def vertical_solution(text, pattern):
    string = ""
    counter = 0
    columns = len(text[0])
    for i in range(columns):
        string = ""
        for _, val in enumerate(text):
            string += val[i]
            if len(string) == len(pattern):
                m = re.match(string, pattern)
                if m is not None:
                    counter += 1
                m = re.match(string, pattern[::-1])
                if m is not None:
                    counter += 1
                string = string[1:]
    return counter


def main_diagonal_solution(text, pattern):
    columns = len(text[0])
    rows = len(text)
    diagonals = []
    line = ""
    for col in range(columns):
        for row in range(rows):
            line = ""
            helper = 0
            if col == 0:
                while row+helper < rows and col+helper < columns:
                    line += (text[row+helper])[col+helper]
                    helper += 1
                diagonals.append(list(line))
            elif row == 0:
                while row+helper < rows and col+helper < columns:
                    line += (text[row+helper])[col+helper]
                    helper += 1
                diagonals.append(list(line))
    return horizontal_solution(diagonals,pattern)


def secondary_diagonal_solution(text, pattern):
    columns = len(text[0])
    rows = len(text)
    diagonals = []
    line = ""
    for col in range(columns):
        for row in range(rows):
            line = ""
            helper = 0
            if col == 0:
                while row-helper >= 0 and col+helper < columns:
                    line += (text[row-helper])[col+helper]
                    helper += 1
                diagonals.append(list(line))
            elif row == rows-1:
                while row-helper >= 0 and col+helper < columns:
                    line += (text[row-helper])[col+helper]
                    helper += 1
                diagonals.append(list(line))
    return horizontal_solution(diagonals, pattern)

def solution_p1(text,pattern):
    solution = 0
    solution += horizontal_solution(text, pattern)
    solution += vertical_solution(text, pattern)
    solution += main_diagonal_solution(text, pattern)
    solution += secondary_diagonal_solution(text, pattern)
    return solution

def a_match(text:list):
    count = 0
    for i,row in enumerate(text):
        if i>0 and i<len(text)-1:
            for j,val in enumerate(row):
                if j>0 and j<len(text[0])-1:
                    if val == "A":
                        if ((text[i-1])[j-1]=="M" and (text[i+1])[j+1]=="S") or ((text[i-1])[j-1]=="S" and (text[i+1])[j+1]=="M"):
                            if ((text[i-1])[j+1]=="M" and (text[i+1])[j-1]=="S") or ((text[i-1])[j+1]=="S" and (text[i+1])[j-1]=="M"):
                                count+=1
    return count

if __name__ == "__main__":
    f = open("inputs/day4.txt")
    string = f.readlines()
    f.close()
    text = find_pattern(string)
    print(solution_p1(text,"XMAS"))
    print(a_match(text))
