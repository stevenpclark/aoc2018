class Marble(object):
    def __init__(self, val, neighbors=None):
        self.val = val
        if neighbors:
            self.left, self.right = neighbors
            self.left.right = self
            self.right.left = self
        else:
            self.left = self
            self.right = self

    def remove(self):
        self.left.right, self.right.left  = self.right, self.left
        return self.val

    def get_left(self, n):
        result = self
        for i in range(n):
            result = result.left
        return result

    def print_ring(self, curr_marble):
        m = self
        while True:
            if m is curr_marble:
                print('(%d)'%m.val, end=' ')
            else:
                print(' %d '%m.val, end=' ')
            m = m.right
            if m is self:
                print()
                break

def solve(num_players, last_marble):
    curr_marble = Marble(0)
    zero_marble = curr_marble
    curr_player = 0
    scores = [0]*num_players
    for val in range(1,last_marble+1):
        #zero_marble.print_ring(curr_marble)
        if val % 23 == 0:
            scores[curr_player] += val
            curr_marble = curr_marble.get_left(6)
            scores[curr_player] += curr_marble.left.remove()
        else:
            left = curr_marble.right
            right = left.right
            curr_marble = Marble(val, (left, right))
        curr_player = (curr_player+1)%num_players

    return max(scores)

def main():
    #print(solve(9, 25))
    #print(solve(10, 1618))
    print(solve(468, 71843))
    print(solve(468, 7184300))

if __name__ == '__main__':
    main()

