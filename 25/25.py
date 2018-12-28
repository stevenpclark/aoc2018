from itertools import combinations, product
from scipy.spatial.distance import cityblock
import random


def main():
    grps = []
    for li in open('input.txt', 'r'):
        grps.append([tuple(int(s) for s in li.split(','))])

    print(len(grps))
    stable = False
    while not stable:
        print(len(grps))
        stable = True
        random.shuffle(grps)
        for g1, g2 in combinations(grps,2):
            #print(g1, g2)
            for p1, p2 in product(g1, g2):
                if cityblock(p1,p2) <= 3:
                    g1.extend(g2)
                    #print('grps:', grps)
                    #print('g2:',g2)
                    grps.remove(g2)
                    stable = False
                    break
            if not stable:
                break

    print(len(grps))

                    




if __name__ == '__main__':
    main()
