from operator import attrgetter
from itertools import chain
import numpy as np

EMPTY, WALL, ELF, GOBLIN = ['.', '#', 'E', 'G']
pos_sorter = attrgetter('pos')
health_sorter = attrgetter('health')

class NPC(object):
    def __init__(self, r, c, race, health=200, power=3):
        self.r = r
        self.c = c
        self.race = race
        self.health = health
        self.power = power

    @property
    def pos(self):
        return (self.r, self.c)

    @pos.setter
    def pos(self, pos):
        self.r, self.c = pos

    def is_alive(self):
        return self.health > 0

    def find_targets(self, npcs):
        return [x for x in npcs if x.race!=self.race and x.is_alive()]

    def take_turn(self, targets, grid):
        in_range_targets = [t for t in targets if self.in_range(t)]
        if not in_range_targets:
            if not self.attempt_move(targets, grid):
                return
            in_range_targets = [t for t in targets if self.in_range(t)]

        if in_range_targets:
            in_range_targets.sort(key=health_sorter)
            self.attack(in_range_targets[0], grid)

    def attempt_move(self, targets, grid):
        move_goals = set([p for t in targets for p in get_empty_neighbors(t.pos, grid)])
        if not move_goals:
            return False
        scratch = np.copy(grid)
        closest_move_goals = grow({self.pos}, move_goals, scratch)
        if not closest_move_goals:
            return False
        move_goal = sorted(list(closest_move_goals))[0]

        #now figure out which way to move towards goal
        scratch = np.copy(grid)
        next_moves = grow({move_goal}, set(get_empty_neighbors(self.pos, grid)), scratch)
        next_pos = sorted(next_moves)[0]
        #print(self.pos, next_move, move_goal)
        grid[self.pos] = '.'
        self.r, self.c = next_pos
        grid[self.pos] = self.race

        return True

    def in_range(self, other):
        return abs(self.r-other.r)+abs(self.c-other.c) <= 1

    def attack(self, other, grid):
        other.health -= self.power
        if other.health <= 0:
            grid[other.pos] = EMPTY

def get_empty_neighbors(pos, grid):
    #assume can only ever be on an interior grid location
    r,c = pos
    neighbors = [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]
    return [p for p in neighbors if grid[p]==EMPTY]

def grow(boundary_set, test_set, scratch):
    if not boundary_set:
        return set()

    found_set = set.intersection(boundary_set, test_set)
    if found_set:
        return found_set

    for p in boundary_set:
        scratch[p] = '#'

    new_boundary_set = set([p for pos in boundary_set for p in get_empty_neighbors(pos, scratch)])
    return grow(new_boundary_set, test_set, scratch)





def main():
    fn = 'input.txt'

    elf_power = 3
    while True:
        print(elf_power)
        grid = np.char.array([list(li.strip()) for li in open(fn,'r')])
        npcs = []
        for (r,c), x in np.ndenumerate(grid):
            if x == ELF:
                npcs.append(NPC(r,c,x,power=elf_power))
            elif x == GOBLIN:
                npcs.append(NPC(r,c,x))
        num_starting_elves = len([npc for npc in npcs if npc.race==ELF])

        done = False
        num_rounds = 0
        while not done:
            #print(grid)
            npcs.sort(key=pos_sorter)
            for npc in npcs:
                if not npc.is_alive():
                    continue
                targets = npc.find_targets(npcs)
                if not targets:
                    done = True
                    break
                npc.take_turn(targets, grid)
            else:
                num_rounds += 1
            npcs = [npc for npc in npcs if npc.is_alive()]
            #input()
        #print(grid)
        npcs = [npc for npc in npcs if npc.is_alive()]
        print(num_rounds*sum([npc.health for npc in npcs]))
        num_surviving_elves = len([npc for npc in npcs if npc.race==ELF])
        #print(num_starting_elves, ' -> ', num_surviving_elves)

        if num_surviving_elves == num_starting_elves:
            break
        else:
            elf_power += 1


if __name__ == '__main__':
    main()
