a = 0
#d = 888
d = 10551288

#for e in range(1,d+1):
    #for b in range(1,d+1):
        #if b*e == d:
            ##print(e)
            #a += e

#print(a)

a = 0
for e in range(1,d+1):
    if d%e==0:
        a += e

print(a)
