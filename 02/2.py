from collections import Counter
from itertools import combinations

def part1(box_strs):
    num_doubles = 0
    num_triples = 0
    for s in box_strs:
        counter = Counter(s)
        counts = counter.values()
        if 2 in counts:
            num_doubles += 1
        if 3 in counts:
            num_triples += 1

    return num_doubles*num_triples


def part2(box_strs):
    for s1, s2 in combinations(box_strs,2):
        similar_string = strings_similar(s1, s2)
        if similar_string:
            return similar_string


def strings_similar(s1, s2):
    #if the number of mismatched chars is exactly 1,
    #return the common string without that char
    #otherwise return False
    num_mismatches = 0
    matching_chars = []
    for c1,c2 in zip(s1,s2):
        if c1!=c2:
            num_mismatches += 1
            if num_mismatches > 1:
                return False
        else:
            matching_chars.append(c1)
    if num_mismatches != 1:
        return False
    else:
        return ''.join(matching_chars)


def main():
    f = open('input.txt', 'r')
    box_strs = [s.strip() for s in f.readlines()]
    f.close()

    print(part1(box_strs))
    print(part2(box_strs))

if __name__ == '__main__':
    main()
