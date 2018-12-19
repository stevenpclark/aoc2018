import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def get_neighbors8(r,c,nr,nc):
    neighbors = []
    if r>0:
        neighbors.append((r-1,c))
        if c>0:
            neighbors.append((r-1,c-1))
        if c<nc-1:
            neighbors.append((r-1,c+1))
    if r<nr-1:
        neighbors.append((r+1,c))
        if c>0:
            neighbors.append((r+1,c-1))
        if c<nc-1:
            neighbors.append((r+1,c+1))
    if c>0:
        neighbors.append((r,c-1))
    if c<nc-1:
        neighbors.append((r,c+1))
    return neighbors



def main():
    fn = 'input.txt'
    grid = np.char.array([list(li.strip()) for li in open(fn,'r')])

    nr,nc = grid.shape

    print(grid)
    #n = 1000
    #n = 1000000000
    n = 720
    xs, ys = [], []
    for i in tqdm(range(n)):
        grid2 = np.copy(grid)
        for (r,c), x in np.ndenumerate(grid):
            n_vals = [grid[p] for p in get_neighbors8(r,c,nr,nc)]
            #print(len(n_vals))
            if x == '.' and n_vals.count('|')>=3:
                grid2[r,c] = '|'
            elif x == '|' and n_vals.count('#')>=3:
                grid2[r,c] = '#'
            elif x == '#':
                if n_vals.count('#')>=1 and n_vals.count('|')>=1:
                    pass
                else:
                    grid2[r,c] = '.'
        grid = np.copy(grid2)
        #print()
        #print(grid)
        unique, counts = np.unique(grid, return_counts=True)
        count_map = dict(zip(unique,counts))
        total = count_map['|']*count_map['#']
        #print(total)
        xs.append(i)
        ys.append(total)

    #plt.plot(xs,ys)
    #plt.show()
    print(total)


    


if __name__ == '__main__':
    main()
