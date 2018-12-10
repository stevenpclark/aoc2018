from collections import Counter

class Pattern(object):
    def __init__(self, index, x, y, dx, dy):
        self.index = index
        self.pos_tuples = []
        for xi in range(x,x+dx):
            for yi in range(y,y+dy):
                self.pos_tuples.append((xi,yi))

    def all_pos_unique(self, pos_counter):
        return all([pos_counter[pos]==1 for pos in self.pos_tuples])


def parse_patterns(lines):
    #TODO switch to RE
    patterns = []
    for li in lines:
        fields = li.split()
        index = fields[0][1:]
        pos_fields = fields[2][:-1].split(',')
        size_fields = fields[3].split('x')
        x,y = [int(s) for s in pos_fields]
        dx,dy = [int(s) for s in size_fields]

        patterns.append(Pattern(index,x,y,dx,dy))
    return patterns


def get_pos_counter(patterns):
    pos_counter = Counter()
    for pat in patterns:
        for pos in pat.pos_tuples:
            pos_counter[pos] += 1
    return pos_counter


def part1(patterns):
    pos_counter = get_pos_counter(patterns)
    overlapped_pos = [k for k,v in pos_counter.items() if v >= 2]
    return len(overlapped_pos)


def part2(patterns):
    pos_counter = get_pos_counter(patterns)
    for pat in patterns:
        if pat.all_pos_unique(pos_counter):
            return pat.index



def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    patterns = parse_patterns(lines)

    print(part1(patterns))
    print(part2(patterns))


if __name__ == '__main__':
    main()
