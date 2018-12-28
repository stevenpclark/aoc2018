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

def main():
    program_ops = []
    ip_reg = None
    ip = 0
    f = open('input.txt', 'r')
    while True:
        li = f.readline()
        if not li:
            break
        fields = li.split()
        if fields[0] == '#ip':
            ip_reg = int(fields[1])
            continue
        assert len(fields)==4
        cmd = fields[0]
        a,b,c = [int(s) for s in fields[1:]]
        program_ops.append((cmd,a,b,c))
    f.close()

    num_ops = len(program_ops)
    print('num program ops: ', num_ops)

    r = [0]*6
    #r[0] = 1 #part2
    r[0] = 1483
    prev_min = 1e9
    while 0<=ip<num_ops:
        if ip == 28:
            if r[2] < prev_min:
                print(r[2])
                prev_min = r[2]
        r[ip_reg] = ip
        op = program_ops[ip]
        cmd, a, b, c = op
        #r_before = r[:]
        r = globals()[cmd](r, a, b, c)
        #print(ip, r_before, op, r)
        ip = r[ip_reg]+1

    print(r[0])


if __name__ == '__main__':
    main()
