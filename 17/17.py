import numpy as np
from PIL import Image

SAND, FLOW, POOL, CLAY = range(4)
colors = np.array([[0,0,0],[0,180,255],[0,0,255],[150,100,0]], dtype=np.uint8)

def do_flow(grid, r, c, r_max):
    assert grid[r,c] == SAND
    r_start = r
    while r <= r_max:
        assert grid[r,c] in [SAND, FLOW], (r,c,grid[r,c], r-r_start)
        grid[r,c] = FLOW
        if r == r_max:
            return
        if grid[r+1,c] != SAND:
            break
        r+=1

    while True:
        if grid[r+1,c] < POOL:
            break
        fill = do_pool(grid, r, c, r_max)
        r -= 1


def do_pool(grid, r, c, r_max):
    #assert grid[r,c]<=FLOW, grid[r,c]
    if grid[r,c] >= POOL:
        return
    #underneath p is either POOL or CLAY (same behavior either way)
    #find L and R boundaries
    c_l, l_blocked = find_edge(grid, r, c, -1)
    c_r, r_blocked = find_edge(grid, r, c, 1)
    if l_blocked and r_blocked:
        fill = POOL
    else:
        fill = FLOW
    #pw, ph = 36,10
    #neighborhood = grid[r-ph//2:r+ph//2,c-pw//2:c+pw//2]
    #print()
    #print(neighborhood)
    grid[r,c_l:c_r+1] = fill
    if not l_blocked:
        grid[r,c_l] = SAND
        do_flow(grid, r, c_l, r_max)
    if not r_blocked:
        grid[r,c_r] = SAND
        do_flow(grid, r, c_r, r_max)


def find_edge(grid, r, c, dc):
    #advance in dc direction until last valid fill square
    #return (c, blocked) (i.e. (int, bool))
    while True:
        if grid[r+1,c] < POOL:
            return (c, False)
        if grid[r,c+dc] == CLAY:
            return (c, True)
        c += dc


def solve(fn,start_col=500):
    f = open(fn, 'r')
    lines = f.readlines()
    f.close()

    r_min, r_max = 1e9, 0
    c_min, c_max = 1e9, -1e9

    tups = []
    for li in lines:
        li = li.replace('=',' ').replace(',','').replace('..',' ')
        fields = li.split()
        assert len(fields) == 5
        a = [int(fields[1])]
        b = range(int(fields[3]),int(fields[4])+1)
        if fields[0] == 'y':
            r,c = a,b
        else:
            r,c = b,a
        tups.append((r,c))
        r_min = min(r_min, min(r))
        r_max = max(r_max, max(r))
        c_min = min(c_min, min(c))
        c_max = max(c_max, max(c))

    r_dim = r_max+1
    c_dim = c_max+2
    grid = np.ones((r_dim, c_dim),dtype=np.uint8)*SAND
    for p in tups:
        grid[p] = CLAY

    last_total = 0
    do_flow(grid, 0, start_col, r_max)

    color_grid = colors[grid[r_min:r_max+1, c_min:c_max]]
    print(color_grid.shape)
    img = Image.fromarray(color_grid,'RGB')
    img.save('flow.png')

    unique, counts = np.unique(grid[r_min:r_max+1, :], return_counts=True)
    count_map = dict(zip(unique,counts))
    total = count_map.get(POOL,0)+count_map.get(FLOW,0)
    stable = count_map.get(POOL,0)
    return (total, stable)


def check(fn, expected, min_start_col=500, max_start_col=500):
    for start_col in range(min_start_col, max_start_col+1):
        total,stable = solve(fn, start_col)
        assert total == expected, '%s got %d expected %d!'%(fn, total,expected)
        print('%s @ %d = %d as expected'%(fn, start_col, total))


def main():
    #check('test1.txt', 57, 499, 501)
    #check('test2.txt', 50, 498, 505)
    #check('test5.txt', 3, 499, 501)
    print(solve('input.txt'))

if __name__ == '__main__':
    main()

