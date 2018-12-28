import matplotlib.pyplot as plt

a = 0
b = 0
c = 0
d = 0
f = 0

f = c | 65536
c = 5234604 

#prev_min = 1e9

s = set()

try:
    while True:
        d = f & 255
        c += d
        c = c & 16777215
        c *= 65899
        c = c & 16777215
        if f<256:
            #print(c)
            #vals.append(c)
            #if c < prev_min:
            if c not in s:
                print(c)
                #prev_min = c
                s.add(c)
            if c==a:
                break
            f = c | 65536
            c = 5234604 
        else:
            d = 0
            while True:
                if ((d+1)*256)<=f:
                    d += 1
                else:
                    f = d
                    break
except KeyboardInterrupt:
    pass

#plt.plot(vals)
#plt.show()
