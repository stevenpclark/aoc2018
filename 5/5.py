import string
from pprint import pprint

def chars_match(c1, c2):
    return abs(ord(c1)-ord(c2)) == 32


def react(p):
    stable = False
    p_len = len(p)
    while not stable:
        stable = True
        i=0
        while i < p_len-1:
            if chars_match(p[i], p[i+1]):
                del p[i:i+2]
                stable = False
                p_len -= 2
            else:
                i += 1

    return len(p)


def main():
    f = open('input.txt', 'r')
    s = f.read().strip()
    f.close()

    #s = 'dabAcCaCBAcCcaDA'

    p = list(s)

    print(react(p))

    pairs = zip(string.ascii_lowercase, string.ascii_uppercase)
    #pairs = zip('abcd','ABCD')
    variant_lens = []
    for c1,c2 in pairs:
        s2 = s.replace(c1,'').replace(c2,'')
        variant_len = react(list(s2))
        #print(variant_len)
        variant_lens.append(variant_len)

    print(min(variant_lens))


if __name__ == '__main__':
    main()
