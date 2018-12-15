#TODO: refactor shared code...

def part1():
    num_warmup = 77201
    num_extracted = 10
    a_ind, b_ind = 0,1
    arr = [3,7]

    while len(arr) < num_warmup+num_extracted:
        a, b = arr[a_ind], arr[b_ind]
        dig_sum = a+b
        tens = dig_sum//10
        ones = dig_sum%10
        if tens:
            arr.append(tens)
        arr.append(ones)
        a_ind = (a_ind+1+a)%len(arr)
        b_ind = (b_ind+1+b)%len(arr)
        #print(arr)
    print(''.join([str(x) for x in arr[-10:]]))


def part2():
    target = [0,7,7,2,0,1]
    nt = len(target)
    a_ind, b_ind = 0,1
    arr = [3,7]

    while True:
        a, b = arr[a_ind], arr[b_ind]
        dig_sum = a+b
        tens = dig_sum//10
        ones = dig_sum%10
        if tens:
            arr.append(tens)
            if arr[-nt:] == target:
                print(len(arr)-nt)
                return
        arr.append(ones)
        if arr[-nt:] == target:
            print(len(arr)-nt)
            return
        a_ind = (a_ind+1+a)%len(arr)
        b_ind = (b_ind+1+b)%len(arr)
        #print(arr)
    print(''.join([str(x) for x in arr[-10:]]))

if __name__ == '__main__':
    #part1()
    part2()
