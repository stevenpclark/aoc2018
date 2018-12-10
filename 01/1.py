def part1(numbers):
    return sum(numbers)

def part2(numbers):
    running_sum = 0
    seen = set()
    seen.add(running_sum)
    while True:
        for n in numbers:
            running_sum += n
            if running_sum in seen:
                return running_sum
            seen.add(running_sum)


def main():
    f = open('input.txt', 'r')
    numbers = [int(s) for s in f.readlines()]
    f.close()
    #numbers = [1, -2, 3, 1]

    print(part1(numbers))
    print(part2(numbers))

if __name__ == '__main__':
    main()
