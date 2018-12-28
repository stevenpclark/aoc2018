import numpy as np


def dist(x1, y1, z1, x2, y2, z2):
    #manhattan
    return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)


def num_in_range(x1,y1,z1, pts):
    count = 0
    for x2,y2,z2,r2 in pts:
        if dist(x1, y1, z1, x2, y2, z2) <= r2:
            count += 1
    return count

def num_in_range2(x1,y1,z1,r1, pts):
    count = 0
    for x2,y2,z2,_ in pts:
        if dist(x1, y1, z1, x2, y2, z2) <= r1:
            count += 1
    return count

def main():
    pts = []
    for li in open('input.txt', 'r'):
        ss = li.replace(',',' ').replace('<',' ').replace('>',' ').replace('=',' ').split()
        pts.append((int(ss[1]),int(ss[2]),int(ss[3]),int(ss[5])))

    max_r = 0
    p1 = None
    xs = []
    ys = []
    zs = []
    rs = []
    for p in pts:
        x,y,z,r = p
        xs.append(x)
        ys.append(y)
        zs.append(z)
        rs.append(r)
        if max_r < r:
            max_r = r
            p1 = p

    print(num_in_range2(*p1,pts))

    print('num pts', len(pts))

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    min_z, max_z = min(zs), max(zs)
    min_r, max_r = min(rs), max(rs)

    print('x', min_x, max_x, max_x-min_x)
    print('y', min_y, max_y, max_y-min_y)
    print('z', min_z, max_z, max_z-min_z)
    print('r', min_r, max_r, max_r-min_r)

    x_span = 1+max_x-min_x
    y_span = 1+max_y-min_y
    z_span = 1+max_z-min_z
    x = (min_x+max_x)//2
    y = (min_y+max_y)//2
    z = (min_z+max_z)//2

    span_divisor = 2

    while True:
        xs = range(x-x_span//2, x+x_span//2, max(1,x_span//16))
        ys = range(y-y_span//2, y+y_span//2, max(1,y_span//16))
        zs = range(z-z_span//2, z+z_span//2, max(1,z_span//16))
        
        vals = np.zeros((len(xs),len(ys),len(zs)),dtype=np.uint16)
        for ix, x in enumerate(xs):
            for iy, y in enumerate(ys):
                for iz, z in enumerate(zs):
                    vals[ix,iy,iz] = num_in_range(x,y,z,pts)
        if vals.shape == (8,8,8):
            break
        ix,iy,iz = np.unravel_index(np.argmax(vals), vals.shape)
        x = xs[ix]
        y = ys[iy]
        z = zs[iz]
        print(x,y,z, vals[ix,iy,iz])
        x_span = max(8, x_span//span_divisor)
        y_span = max(8, y_span//span_divisor)
        z_span = max(8, z_span//span_divisor)

    max_val = vals.max()
    print(max_val)

    dists = []
    for (ix,iy,iz),v in np.ndenumerate(vals):
        if v == max_val:
            dists.append(abs(xs[ix])+abs(ys[iy])+abs(zs[iz]))
    print(min(dists))





if __name__ == '__main__':
    main()
