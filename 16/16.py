cmds = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def addr(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]+r[b]
    return r2

def addi(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]+b
    return r2

def mulr(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]*r[b]
    return r2

def muli(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]*b
    return r2

def banr(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]&r[b]
    return r2

def bani(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]&b
    return r2

def borr(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]|r[b]
    return r2

def bori(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]|b
    return r2

def setr(r, a, b, c):
    r2 = r[:]
    r2[c] = r[a]
    return r2

def seti(r, a, b, c):
    r2 = r[:]
    r2[c] = a
    return r2

def gtir(r, a, b, c):
    r2 = r[:]
    r2[c] = int(a>r[b])
    return r2

def gtri(r, a, b, c):
    r2 = r[:]
    r2[c] = int(r[a]>b)
    return r2

def gtrr(r, a, b, c):
    r2 = r[:]
    r2[c] = int(r[a]>r[b])
    return r2

def eqir(r, a, b, c):
    r2 = r[:]
    r2[c] = int(a==r[b])
    return r2

def eqri(r, a, b, c):
    r2 = r[:]
    r2[c] = int(r[a]==b)
    return r2

def eqrr(r, a, b, c):
    r2 = r[:]
    r2[c] = int(r[a]==r[b])
    return r2

def get_num_matching_cmds(sample):
    r1, op, r2 = sample
    op_code, a, b, c = op
    num_matching = 0
    for cmd in cmds:
        if r2 == globals()[cmd](r1, a, b, c):
            num_matching += 1
    return num_matching


def assign(ordered_cmds, op_code_map, i=0):
    if i>=16:
        return True
    possible_cmds = [cmd for cmd in op_code_map[i] if cmd not in ordered_cmds]
    if not possible_cmds:
        return False
    for cmd in possible_cmds:
        ordered_cmds[i] = cmd
        if assign(ordered_cmds, op_code_map, i+1):
            return True
    ordered_cmds[i] = None
    return False


def main():
    samples = []
    program_ops = []
    f = open('input.txt', 'r')
    while True:
        li1 = f.readline()
        if 'Before' not in li1:
            break
        li2 = f.readline()
        li3 = f.readline()
        f.readline()
        r1 = [int(s) for s in li1.replace('[','').replace(']','').replace(',','').split()[1:]]
        op = [int(s) for s in li2.split()]
        r2 = [int(s) for s in li3.replace('[','').replace(']','').replace(',','').split()[1:]]
        samples.append((r1,op,r2))

    while True:
        li = f.readline()
        if not li:
            break
        op = [int(s) for s in li.split()]
        if len(op) == 4:
            program_ops.append(op)
    f.close()
    print('num samples: ', len(samples))
    print('num program ops: ', len(program_ops))

    part1 = 0
    for sample in samples:
        if get_num_matching_cmds(sample) >= 3:
            part1 += 1
    print(part1)

    op_code_map = {op_code:cmds[:] for op_code in range(16)}
    for r1, op, r2 in samples:
        op_code, a, b, c = op
        possible_cmds = op_code_map[op_code]
        for cmd in possible_cmds[:]:
            if r2 != globals()[cmd](r1, a, b, c):
                possible_cmds.remove(cmd)

    ordered_cmds = [None]*16
    assert assign(ordered_cmds, op_code_map)

    r = [0]*4
    for op_code, a, b, c in program_ops:
        cmd = ordered_cmds[op_code]
        r = globals()[cmd](r, a, b, c)

    print(r[0])
    

if __name__ == '__main__':
    main()
