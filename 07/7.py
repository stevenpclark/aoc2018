from collections import defaultdict

def main():
    blockers = defaultdict(list)
    step_set = set()
    for li in open('input.txt'):
        fields = li.split()
        before = fields[1]
        after = fields[7]
        blockers[after].append(before)
        step_set.add(before)
        step_set.add(after)

    num_steps = len(step_set)
    num_workers = 5
    worker_map = dict()
    result = []
    t = 0

    while len(result) < num_steps:
        ready = [x for x in step_set if not blockers[x]]
        ready.sort()

        #dole out ready list to workers, remove them from step_set
        for r in ready:
            if len(worker_map) >= num_workers:
                break
            time_required = 60+ord(r)-64
            worker_map[r] = time_required
            step_set.remove(r)

        #advance time, resolve
        t += 1
        for c in list(worker_map.keys()):
            worker_map[c] -= 1
            if worker_map[c] == 0:
                worker_map.pop(c)
                result.append(c)
                for li in blockers.values():
                    try:
                        li.remove(c)
                    except ValueError:
                        pass

    print(''.join(result))
    print(t)




if __name__ == '__main__':
    main()


