import numpy as np

def parse_input(fn):
    f = open(fn, 'r')
    lines = sorted(f.readlines())
    f.close()

    num_nights = len([s for s in lines if 'shift' in s])

    guard_ids = set()
    guard_map = np.zeros((num_nights,),dtype=int)
    sleep_map = np.zeros((num_nights,60), dtype=bool)

    sleep_time = None

    r = -1
    for li in lines:
        fields = li.split()
        t = int(fields[1][3:5])
        if 'shift' in li:
            if sleep_time is not None:
                #prev day slept all the way to end?
                sleep_map[r,sleep_time:] = True
                sleep_time = None

            r += 1
            guard_id = int(fields[3][1:])
            guard_ids.add(guard_id)
            guard_map[r] = guard_id
        elif 'asleep' in li:
            sleep_time = t
        elif 'wakes' in li:
            assert sleep_time is not None
            sleep_map[r,sleep_time:t] = True
            sleep_time = None

    if sleep_time is not None:
        #final day slept all the way to end?
        sleep_map[r,sleep_time:] = True
        sleep_time = None

    return guard_ids, guard_map, sleep_map


def part1(guard_ids, guard_map, sleep_map):
    guard_sleep_total_map = dict()
    for guard_id in guard_ids:
        guard_rows = sleep_map[guard_map==guard_id,:]
        guard_sleep_total_map[guard_id] = guard_rows.sum()

    sleepy_guard = max(guard_sleep_total_map, key=guard_sleep_total_map.get)
    sleepy_guard_rows = sleep_map[guard_map==sleepy_guard,:]
    sleepy_times = sleepy_guard_rows.sum(axis=0)
    sleepiest_minute = sleepy_times.argmax()

    return sleepy_guard*sleepiest_minute

def part2(guard_ids, guard_map, sleep_map):
    result_list = []
    for guard_id in guard_ids:
        guard_rows = sleep_map[guard_map==guard_id,:]
        sleepy_times = guard_rows.sum(axis=0)
        sleepiest_minute = sleepy_times.argmax()
        result_list.append((sleepy_times[sleepiest_minute], sleepiest_minute*guard_id))

    result_list.sort()
    return result_list[-1][-1]


def main():
    inputs = parse_input('input.txt')

    print(part1(*inputs))
    print(part2(*inputs))


if __name__ == '__main__':
    main()

