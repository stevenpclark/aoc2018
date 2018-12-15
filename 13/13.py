#use r,c notation (i.e. y,x) for simple sorting
#[r,c,dr,dc,turn_state, active]

vel_map = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
STRAIGHT, LEFT, RIGHT = range(3)

def turn(s, dr, dc, turn_state):
    turn_type = STRAIGHT
    if s == '/':
        #if going u/d, this is a R turn. if going l/r, this is a L turn
        turn_type = [LEFT, RIGHT][bool(dr)]
    elif s == '\\':
        #if going u/d, this is a L turn. if going l/r, this is a R turn
        turn_type = [LEFT, RIGHT][bool(dc)]
    elif s == '+':
        turn_type = [LEFT, STRAIGHT, RIGHT][turn_state]
        turn_state = (turn_state+1)%3

    if turn_type == LEFT:
        dr, dc = -dc, dr
    elif turn_type == RIGHT:
        dr, dc = dc, -dr

    return dr, dc, turn_state


def solve(lines, karts):
    while True:
        karts.sort()
        for k, kart in enumerate(karts):
            r,c,dr,dc,turn_state,active = kart
            if not active:
                continue
            r,c = r+dr,c+dc
            s = lines[r][c]
            dr,dc,turn_state = turn(lines[r][c], dr, dc, turn_state)

            #collision check:
            for kart2 in karts:
                if not kart2[-1]: #only check active karts
                    continue
                if [r,c] == kart2[0:2]:
                    print('Collision at %d,%d'%(c,r))
                    kart2[-1] = False
                    active = False
                    break
            karts[k] = [r,c,dr,dc,turn_state,active]

        #filter out inactive karts
        karts = [kart for kart in karts if kart[-1]]
        if len(karts) == 1:
            r,c = karts[0][0:2]
            print('%d,%d'%(c,r))
            break


def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()

    karts = []
    for r, li in enumerate(lines):
        for c, s in enumerate(li):
            if s in vel_map.keys():
                kart = [r,c,*vel_map[s], 0, True]
                #print(kart)
                karts.append(kart)

    solve(lines, karts)


if __name__ == '__main__':
    main()
