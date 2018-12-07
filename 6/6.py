class Patch(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_infinite = False
        self.size = 0

    def dist(self, x2, y2):
        return abs(self.x-x2)+abs(self.y-y2)


def main():
    patches = []
    for line in open('input.txt', 'r'):
        x, y = (int(s) for s in line.split(','))
        patches.append(Patch(x,y))

    xs = [p.x for p in patches]
    ys = [p.y for p in patches]

    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)

    #if a patch reaches the edge of the bbox, it is guaranteed to be infinite. I think.

    num_safe = 0
    for x in range(min_x, max_x+1):
        x_edge = x in [min_x, max_x]
        for y in range(min_y, max_y+1):
            y_edge = y in [min_y, max_y]

            closest_dist = 1e9
            closest_patch = None
            total_distances = 0
            for p in patches:
                dist = p.dist(x,y)
                total_distances += dist
                if dist < closest_dist:
                    closest_dist = dist
                    closest_patch = p
                elif dist == closest_dist:
                    closest_patch = None
            if closest_patch:
                closest_patch.size += 1
                if x_edge or y_edge:
                    closest_patch.is_infinite = True
            if total_distances < 10000:
                num_safe += 1

    #part1:
    finite_sizes = [p.size for p in patches if not p.is_infinite]
    print(max(finite_sizes))

    #part2:
    print(num_safe)



if __name__ == '__main__':
    main()
