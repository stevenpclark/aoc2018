from collections import defaultdict

def main():
    blockers = defaultdict(list)
    step_set = set()
    for li in open('test.txt'):
        fields = li.split()
        before = fields[1]
        after = fields[7]
        blockers[after].append(before)
        step_set.add(before)
        step_set.add(after)

    num_workers = 5
    result = []
    t = 0

    while step_set:
        ready = [x for x in step_set if not blockers[x]]
        ready.sort()
        print(ready[0:5])
        for step in ready[0:5]:
            result.append(step)
            for li in blockers.values():
                try:
                    li.remove(step)
                except ValueError:
                    pass
            step_set.remove(step)
        t += 1

    print(''.join(result))
    print(t)




if __name__ == '__main__':
    main()


