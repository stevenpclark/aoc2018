import numpy as np

GEO_TYPES = [ROCKY, WET, NARROW] = range(3)
TOOLS = [TORCH, GEAR, NEITHER] = range(3)
VALID_TOOL_MAP = {ROCKY:[GEAR,TORCH],WET:[GEAR,NEITHER],NARROW:[TORCH,NEITHER]}
MOVE_COST = 1
SWAP_COST = 7
MAX_VAL = int(1e9)

def get_neighbors4(r,c,nr,nc):
    neighbors = []
    if r>0:
        neighbors.append((r-1,c))
    if r<nr-1:
        neighbors.append((r+1,c))
    if c>0:
        neighbors.append((r,c-1))
    if c<nc-1:
        neighbors.append((r,c+1))
    return neighbors


def solve(depth, target_x, target_y, pad=30):
    nr = target_y+1+pad
    nc = target_x+1+pad
    geo_index = np.zeros((nr, nc), dtype=int)
    erosion = np.zeros((nr, nc), dtype=int)
    nav = np.ones((nr, nc, len(TOOLS)), dtype=int)*MAX_VAL

    for r in range(nr):
        for c in range(nc):
            if r == 0:
                geo_index[r,c] = c*16807
            elif c == 0:
                geo_index[r,c] = r*48271
            elif (r,c) == (target_y,target_x):
                geo_index[r,c] = 0
            else:
                geo_index[r,c] = erosion[r-1,c]*erosion[r,c-1]
            erosion[r,c] = (geo_index[r,c]+depth)%20183

    geo_type = erosion % 3
    risk = geo_type[:target_y+1,:target_x+1].sum()

    nav[0,0,0] = 0

    active_front = set()
    active_front.add((0,0))
    active_front.add((1,0))
    active_front.add((0,1))
    while active_front:
        #print(len(active_front))
        next_active_front = set()
        for r,c in active_front:
            modified = False
            gt = geo_type[r,c]
            valid_tools = VALID_TOOL_MAP[gt]
            n4 = get_neighbors4(r,c,nr,nc)
            for t in valid_tools:
                for r2,c2 in n4:
                    possible_move_val = nav[r2,c2,t]+MOVE_COST
                    if nav[r,c,t] > possible_move_val:
                        nav[r,c,t] = possible_move_val
                        modified = True

            possible_swap_val = min(nav[r,c,:])+SWAP_COST
            for t in valid_tools:
                if nav[r,c,t] > possible_swap_val:
                    nav[r,c,t] = possible_swap_val
                    modified = True
            if modified:
                for r2,c2 in n4:
                    next_active_front.add((r2,c2))
        active_front = next_active_front

    final_costs = nav[target_y,target_x,:]
    final_costs[GEAR] += SWAP_COST
    final_cost = nav[target_y,target_x,:].min()

    #print(risk, final_cost)

    return risk, final_cost


def main():
    assert solve(510, 10, 10, pad=5) == (114,45)
    print(solve(11817, 9, 751, pad=30))

if __name__ == '__main__':
    main()
