import string
from pprint import pprint

def chars_match(c1, c2):
    return abs(ord(c1)-ord(c2)) == 32


def main():
    f = open('input.txt', 'r')
    s = f.read().strip()
    f.close()

    p = list(s)
    p = list('dabAcCaCBAcCcaDA')
    variants = []
    #pairs = zip(string.ascii_lowercase, string.ascii_uppercase)
    pairs = zip('abcd','ABCD')
    for c1,c2 in pairs:
        p2 = p[:]
        p2.remove(c1)
        p2.remove(c2)
        variants.append(p2)

    pprint(variants)

    stable = False
    while not stable:
        for i, c in enumerate(p[:-1]):
            if chars_match(c, p[i+1]):
                del p[i:i+2]
                #print(p)
                break
        else:
            stable = True

    print(len(p))


if __name__ == '__main__':
    main()
