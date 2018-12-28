from operator import attrgetter

initiative_sorter = attrgetter('initiative')

class Group(object):
    def __init__(self, name, count, health, damage, damage_type, initiative, immunities, weaknesses, enemy_team):
        self.name = name
        self.count = count
        self.health = health
        self._damage = damage
        self.damage_type = damage_type
        self.initiative = initiative
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.enemy_team = enemy_team

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        #default sorter
        return (self.effective_power, self.initiative) < (other.effective_power, other.initiative)

    @property
    def effective_power(self):
        return self.count*self._damage

    def check_damage(self, target):
        damage = self.effective_power
        if self.damage_type in target.immunities:
            damage = 0
        elif self.damage_type in target.weaknesses:
            damage *= 2
        return damage

    def attack(self, target):
        if self.count <= 0:
            return 0
        damage = self.check_damage(target)
        target_count_reduction = min(target.count, damage//target.health)
        #print(self.name, 'deals', damage, 'damage to', target.name, 'killing', target_count_reduction)
        target.count -= target_count_reduction
        return target_count_reduction

    def is_alive(self):
        return self.count > 0


def parse_groups(fn):
    home_team = []
    away_team = []

    for li in open(fn,'r'):
        if 'Immune' in li:
            team = home_team
            enemy_team = away_team
            index = 1
            name_pat = 'Immune System group %d'
        elif 'Infection' in li:
            team = away_team
            enemy_team = home_team
            index = 1
            name_pat = 'Infection group %d'
        else:
            li = li.strip()
            if not li:
                continue
            li = li.replace(',','')
            fields = li.split()
            count = int(fields[0])
            health = int(fields[4])
            damage = int(fields[-6])
            damage_type = fields[-5]
            initiative = int(fields[-1])
            weaknesses = []
            immunities = []
            try:
                elems = li.split('(')[1].split(')')[0].split(';')
                for e in elems:
                    if 'immune' in e:
                        stats = immunities
                    else:
                        stats = weaknesses
                    stats.extend(e.split()[2:])
            except IndexError:
                pass
            team.append(Group(name_pat%index, count, health, damage, damage_type, initiative, immunities, weaknesses, enemy_team))
            index += 1
    return home_team, away_team


def select_targets(home_team, away_team):
    #print('select targets')
    #NOTE: modifies sort order of teams
    target_map = dict()
    home_team.sort(reverse=True)
    away_team.sort(reverse=True)
    groups = []
    groups.extend(home_team)
    groups.extend(away_team)
    groups.sort(reverse=True)
    already_targeted = set()

    for g in groups:
        candidate_target_tups = [(g.check_damage(g2), g2) for g2 in g.enemy_team if g2 not in already_targeted]
        for t in candidate_target_tups[:]:
            if t[0] == 0:
                candidate_target_tups.remove(t)
        #print(candidate_target_tups)
        if candidate_target_tups:
            candidate_target_tups.sort(reverse=True)
            target = candidate_target_tups[0][1]
            target_map[g] = target
            already_targeted.add(target)
        else:
            target_map[g] = None
        
    return target_map


def main():
    for boost in range(0,2000):
        #print(boost)
        home_team, away_team = parse_groups('input.txt')
        for g in home_team:
            g._damage += boost

        while home_team and away_team:
            #print()
            #print('Immune:', [g.count for g in home_team])
            #print('Infection:', [g.count for g in away_team])
            target_map = select_targets(home_team, away_team)
            attackers = sorted(target_map.keys(), key=initiative_sorter, reverse=True)
            kills = 0
            #print(target_map)
            for attacker in attackers:
                target = target_map[attacker]
                if target:
                    kills += attacker.attack(target)

            #cleanup phase
            for team in [home_team, away_team]:
                for g in team[:]:
                    if not g.is_alive():
                        team.remove(g)

            if kills == 0:
                print('stalemate detected?')
                break
        away_left = sum([g.count for g in away_team])
        if boost == 0:
            print('part 1:',away_left)
        else:
            home_left = sum([g.count for g in home_team])
            #print(boost, away_left, home_left)
            if away_left == 0:
                print('part 2:', home_left)
                break



if __name__ == '__main__':
    main()
