import sys
import numpy as np

N, E, S, W = range(4)

def solve(x_start, y_start, s, i_start, grid, xc, yc, mask_start=None, mask_stop=0):
    x,y = x_start, y_start
    #print(s, i_start, s[i_start], '(%d,%d)'%(x,y), mask_start, mask_stop)
    for i in range(i_start, len(s)):
        if mask_start and (mask_start<=i<=mask_stop):
            continue
        #print(s, '\t',i, s[i], '(%d,%d)'%(x,y))
        c = s[i]
        if c == '(':
            sep_pos = find_separators(s, i)
            #print('sep_pos', sep_pos)
            #need to spawn workers for each thing in group
            for j, pos in enumerate(sep_pos[:-1]):
                if j < len(sep_pos)-2:
                    solve(x,y,s,pos+1, grid, xc, yc, sep_pos[j+1], max(sep_pos[j+2], mask_stop))
                else:
                    #final one, no need for mask
                    solve(x,y,s,pos+1, grid, xc, yc, mask_start, mask_stop)
            return

        elif c == '|':
            pass
        elif c == ')':
            pass
        elif c == '^':
            pass
        elif c == 'N':
            grid[y+yc,x+xc,N] = True
            y-=1
            grid[y+yc,x+xc,S] = True
        elif c == 'E':
            grid[y+yc,x+xc,E] = True
            x+=1
            grid[y+yc,x+xc,W] = True
        elif c == 'S':
            grid[y+yc,x+xc,S] = True
            y+=1
            grid[y+yc,x+xc,N] = True
        elif c == 'W':
            grid[y+yc,x+xc,W] = True
            x-=1
            grid[y+yc,x+xc,E] = True


def find_separators(s, i_start):
    #assume we're starting on a (
    #return indices of matching |'s and ) too
    r = [i_start]
    level = 1
    for i in range(i_start+1, len(s)):
        c = s[i]
        #print(i, level, c)
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
            if level == 0:
                r.append(i)
                return r
        elif c == '|' and level == 1:
            r.append(i)
    assert False


def main():
    fn = sys.argv[1]
    f = open(fn,'r')
    s = f.read().strip()
    f.close()

    xc, yc = 100, 100
    grid = np.zeros((xc*2,yc*2,4), dtype=bool)
    solve(0,0,s,0, grid, xc, yc)
    vals = np.ones((xc*2,yc*2), dtype=int)*-1

    n_steps = 0
    b_set = set()
    b_set.add((yc,xc))
    while b_set:
        #print('--')
        #print(b_set)
        next_b_set = set()
        for y,x in b_set:
            vals[y,x] = n_steps
            free = grid[y,x,:]
            #print('free', free)
            if free[N]:
                next_b_set.add((y-1,x))
            if free[E]:
                next_b_set.add((y,x+1))
            if free[S]:
                next_b_set.add((y+1,x))
            if free[W]:
                next_b_set.add((y,x-1))
        #print(next_b_set)
        for y,x in list(next_b_set):
            if vals[y,x] != -1:
                next_b_set.remove((y,x))
        #print(next_b_set)

        n_steps += 1
        b_set = next_b_set

    #print(vals)
    print(vals.max())
    print((vals>=1000).sum())


if __name__ == '__main__':
    main()
