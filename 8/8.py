def get_metadata_sum(data, i=0):
    num_children = data[i]
    num_metadata = data[i+1]
    i += 2

    metadata_sum = 0

    child_values = []
    for c in range(num_children):
        dms, i, value = get_metadata_sum(data, i)
        metadata_sum += dms
        child_values.append(value)

    metadata = data[i:i+num_metadata]
    value = sum(metadata)
    metadata_sum += value
    
    if child_values:
        value = 0
        for x in metadata:
            if 1<=x<=num_children:
                value += child_values[x-1]

    return metadata_sum, i+num_metadata, value


def main():
    f = open('input.txt', 'r')
    s = f.read()
    f.close()

    #s = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

    data = [int(x) for x in s.split()]

    metadata_sum, _, value = get_metadata_sum(data)

    print(metadata_sum)
    print(value)


if __name__ == '__main__':
    main()
