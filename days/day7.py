
def load_data():
    f = open("inputs/day7.txt")
    lines = []
    while True:
        text = f.readline().strip()
        if len(text) == 0:
            break
        line = text.split()
        line[0] = line[0].removesuffix(":")
        lines.append(line)
    f.close()
    return lines

def try_combination(line, calculatedNumber, current_iteration, pt2=False):
    concatenation = False
    if current_iteration == 0:
        calculatedNumber = int(line[current_iteration+1])
    if calculatedNumber > int(line[0]):
        return False
    if current_iteration+1 == len(line)-1:
        return calculatedNumber-int(line[0]) == 0
    else:
        plus = try_combination(
            line, calculatedNumber + int(line[current_iteration+2]), current_iteration+1, pt2)
        times = try_combination(
            line, calculatedNumber * int(line[current_iteration+2]), current_iteration+1, pt2)
        if pt2:
            concatenation = try_combination(line, int(
                str(calculatedNumber)+line[current_iteration+2]), current_iteration+1, pt2)
        return plus | times | concatenation


def try_lines(lines):
    sum1 = 0
    sum2 = 0
    for _, line in enumerate(lines):
        if try_combination(line, 0, 0):
            sum1 += int(line[0])
            sum2 += int(line[0])
            continue
        if try_combination(line, 0, 0, True):
            sum2 += int(line[0])
    return sum1, sum2


if __name__ == "__main__":
    lines = load_data()
    print(try_lines(lines))
