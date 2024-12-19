from functools import lru_cache

def load_data():
    f = open("inputs/day19.txt")
    data = f.read().split("\n")
    f.close()
    patterns = data.pop(0).split(", ")
    data.pop(0)
    data.pop(-1)
    return data, patterns


def dictionarize(sequences, patterns):
    containment = {}
    for _, seqence in enumerate(sequences):
        for _, pattern in enumerate(patterns):
            if pattern in seqence:
                if seqence not in containment:
                    containment[seqence] = []
                containment[seqence].append(pattern)
    return containment


def can_build(sequences):
    count = 0
    count2 = 0
    for _, sequence in enumerate(sequences):
        # print(sequence)
        val =  building(sequence, sequences[sequence])
        count2 += val
        if val != 0:
            count += 1
    return count, count2



def building(sequence, patterns):
    patterns = tuple(patterns)

    @lru_cache(None)
    def cachable_building(sequence):
        count = 0
        if sequence == "":
            return 1
        for _, pattern in enumerate(patterns):
            if sequence[:len(pattern)] == pattern:
                count += cachable_building(sequence[len(pattern):])
        return count
    return cachable_building(sequence)

if __name__ == "__main__":
    seqences, patterns = load_data()
    d = dictionarize(seqences, patterns)
    print(can_build(d))
