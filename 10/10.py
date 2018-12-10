import numpy as np

class Point(object):
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def step(self, t=1):
        self.x += t*self.dx
        self.y += t*self.dy


def main():
    pts = []
    for li in open('input.txt', 'r'):
        #TODO replace with RE:
        li = li.replace('<',' ').replace('>',' ').replace(',','')
        fields = li.split()
        x, y, dx, dy = [int(fields[i]) for i in [1,2,4,5]]
        pts.append(Point(x,y,dx,dy))

    prev_x_span = 1e9
    for i in range(1, 20000):
        for pt in pts:
            pt.step()
        xs = [pt.x for pt in pts]
        x_span = max(xs)-min(xs)
        if x_span > prev_x_span:
            #rewind 1 and we're done
            i_best = i-1
            for pt in pts:
                pt.step(-1)
            break
        else:
            prev_x_span = x_span

    xs = [pt.x for pt in pts]
    ys = [pt.y for pt in pts]
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)
    x_span, y_span = max_x-min_x+1, max_y-min_y+1
    grid = np.zeros((y_span, x_span),dtype=int)
    for pt in pts:
        grid[pt.y-min_y,pt.x-min_x] = 1

    chars = (' ','#')
    for r in range(y_span):
        for c in range(x_span):
            print(chars[grid[r,c]], end='')
        print()
    print(i_best)

if __name__ == '__main__':
    main()
