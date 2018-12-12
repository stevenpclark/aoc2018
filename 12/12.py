def parse_input(fn):
    f = open(fn, 'r')
    s = f.read()
    f.close()

    s = s.replace('.', '0').replace('#','1')
    lines = s.split('\n')
    initial_str = lines[0].split()[2]
    initial_state = [int(c) for c in initial_str]

    rules = [0]*32
    for li in lines[2:]:
        if not li:
            break
        fields = li.split(' => ')
        rules[int(fields[0], 2)] = int(fields[1], 2)

    return initial_state, rules


def solve(s, rules, num_gens=20):
    left = 0
    for g in range(num_gens):
        #tidy ends
        while s[-1] == 0:
            s.pop()
        first_plant = s.index(1)
        s = [0,0,0,0]+s[first_plant:]+[0,0,0,0]
        left += first_plant-4

        s_len = len(s)
        new_s = [0]*s_len

        for i in range(s_len-4):
            rule_ind = 16*s[i] + 8*s[i+1] + 4*s[i+2] + 2*s[i+3] + s[i+4]
            new_s[i+2] = rules[rule_ind]
        s = new_s

        total = 0
        for i, x in enumerate(s):
            if x:
                total += (i+left)

        #assume quiets down after a while (goes linear), so short-circuit:
        if g > 1000:
            m = total-prev_total
            b = total-m*(g+1)
            return m*num_gens+b

        prev_total = total

    return total


def main():
    initial_state, rules = parse_input('input.txt')

    print(solve(initial_state, rules, 20))
    print(solve(initial_state, rules, int(50e9)))

if __name__ == '__main__':
    main()
