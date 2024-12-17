from functools import lru_cache


def load_data():
    f = open("inputs/day11.txt")
    stones = f.readline().strip().split()
    f.close()
    return stones


@lru_cache(maxsize=None)
def recursive_blink(stone_value, blink_count_remaining):
    if blink_count_remaining <= 0:
        return 1
    else:
        if stone_value=="0" or stone_value=="":
            return recursive_blink("1", blink_count_remaining-1)
        elif len(stone_value) % 2 == 0:
            sum = 0
            sum += recursive_blink(stone_value[:int(len(stone_value)/2)].lstrip("0"), blink_count_remaining-1)
            sum += recursive_blink(stone_value[int(len(stone_value)/2):].lstrip("0"), blink_count_remaining-1)
            return sum
        else:
            return recursive_blink(str(int(stone_value)*2024).lstrip("0"), blink_count_remaining-1)


if __name__ == "__main__":
    stones = load_data()
    stones = ["1"]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for stone in stones:
        sum1 += recursive_blink(stone, 25)
        sum2 += recursive_blink(stone, 75)
        sum3 += recursive_blink(stone, 998)
    print(sum1, sum2)
    print(sum3)
