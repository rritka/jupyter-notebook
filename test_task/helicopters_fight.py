import math
import random
import matplotlib.pyplot as plt
from scipy.spatial import distance


class Helicopter:
    """This is a helicopter"""

    def __init__(self, speed: float, armor: float, life: float,
                 damage: float, capacity: float, rapidity: float):
        """We init by creating init fields with parameters"""

        # Damage options - damage
        self.damage = damage
        self.capacity = capacity
        self.rapidity = rapidity

        # Armor options - armor
        self.speed = speed
        self.armor = armor
        self.life = life

        self.points = 0

    def access_armor(self):
        """This function access armor of helicopter"""

        access = self.speed * armor['speed'] + self.armor * armor['armor'] + self.life * armor['life']

        return access

    def access_war(self):
        """This function access damage of helicopter"""

        access = self.damage * war['damage'] + self.capacity * war['capacity'] + self.rapidity * war['rapidity']

        return access


# This parameter is for calculating of life after which the helicopter considered to be fall down
repair_rate = 0.1

# This is for accessing the damage
war = {
    'damage': 0.7,
    'capacity': 0.2,
    'rapidity': 0.1
}

# This is for accessing the armor
armor = {
    'speed': 0.1,
    'armor': 0.2,
    'life': 0.7
}

# This is for repair and refill the capacity
price = {
    'repair': 10,
    'fill': 100
}

# This is for reward
reward = {
    'kill': 2,
    'win': 1,
    'noone': 1
}


def access_distance(h1: Helicopter, h2: Helicopter):
    """This function calculates difference between helicopters"""

    x_1 = h1.access_armor()
    x_2 = h2.access_armor()

    y_1 = h1.access_war()
    y_2 = h2.access_war()

    distance = math.sqrt((x_2 - x_1)*(x_2 - x_1) + (y_2 - y_1)*(y_2 - y_1))

    return distance


def access_similarity(d: float, d_max: float):
    """We compare similarity between helicopters"""

    if d <= d_max:
        return True
    else:
        return False


def print_stats(h: Helicopter):
    """This function prints helicopter stats"""

    print('Armor stats:\nSpeed: {}\nArmor: {}\nLife: {}'.format(
        h.speed, h.armor, h.life))
    print('War stats:\nDamage: {}\nCapacity: {}\nRapidity: {}'.format(
        h.damage, h.capacity, h.rapidity))
    print('Helicopter armor usability: {}; war usability: {}\n'.format(h.access_armor(), h.access_war()))


def play_battle(h1: Helicopter, h2: Helicopter, num_1: int, num_2: int, repair_rate: float):
    """This function plays round by round the battle"""

    # Repair ratio
    r1 = h1.access_armor()*repair_rate
    r2 = h2.access_armor()*repair_rate

    # Life ratio
    l1 = h1.access_armor()
    l2 = h2.access_armor()

    # Ammo ratio
    c1 = h1.capacity
    c2 = h2.capacity

    # Damage ratio
    d1 = h1.access_war()
    d2 = h2.access_war()

    print('!!!!!!FIGHT!!!!!!FIGHT!!!!!!FIGHT!!!!!\n')
    print('Helicopter {} VS Helicopter {}\n'.format(num_1, num_2))

    while True:

        # We choose who fire first
        choice = random.randint(0, 100)

        if c1 < 1 or c2 < 1:
            print('Ammunition is ended: no one wins!!!!!')
            h1.points += reward['noone']
            h2.points += reward['noone']
            break

        if abs(choice-h1.rapidity) < abs(choice-h2.rapidity):
            print('Helicopter {} fires:'.format(num_1))

            # We decide whether helicopter miss
            hit = random.randint(0, 1)

            if hit == 0:
                print('Helicopter {} miss!!!'.format(num_1))
            else:
                print('Helicopter {} succeed!!!'.format(num_1))

            l2 -= hit * d1
            c1 -= 1

            if l2 <= 0:
                l2 = 0
                print('Helicopter {} killed\n'.format(num_2))
                print('!!!!!!!!!!!!!!!!!!!')
                print('Helicopter {} wins!!!'.format(num_1))
                print('Helicopter {} gets {} points'.format(num_1, reward['kill']))
                h1.points += reward['kill']
                break

            elif l2 <= r2:
                print('Helicopter {} fall down\n'.format(num_2))
                print('!!!!!!!!!!!!!!!!!!!')
                print('Helicopter {} wins!!!'.format(num_1))
                print('Helicopter {} gets {} points'.format(num_1, reward['win']))
                h1.points += reward['win']
                l2 = 0
                break

            else:
                print('Helicopter {} survived: life left: {};  ammo left: {}'.format(num_2, l2, c2))

        else:
            print('Helicopter {} fires:'.format(num_2))

            # We decide whether helicopter miss
            hit = random.randint(0, 1)

            if hit == 0:
                print('Helicopter {} miss!!!'.format(num_2))
            else:
                print('Helicopter {} succeed!!!'.format(num_2))

            l1 -= hit * d2
            c2 -= 1

            if l1 <= 0:
                print('Helicopter {} killed\n'.format(num_1))
                print('!!!!!!!!!!!!!!!!!!!')
                print('Helicopter {} wins!!!'.format(num_2))
                print('Helicopter {} gets {} points'.format(num_2, reward['kill']))
                l1 = 0
                h2.points += reward['kill']
                break

            elif l1 <= r1:
                print('Helicopter {} fall down\n'.format(num_1))
                print('!!!!!!!!!!!!!!!!!!!')
                print('Helicopter {} wins!!!'.format(num_2))
                print('Helicopter {} gets {} points'.format(num_2, reward['win']))
                h2.points += reward['win']
                l1 = 0
                break

            else:
                print('Helicopter {} survived: life left: {}; ammo left: {}'.format(num_1, l1, c1))

    print('==================================================================')
    print('Helicopter {}:\nprice for refilling ammo: {}\nprice for repairing: {}\n'.format(num_1,
            (h1.capacity-c1)*price['fill'], round(abs(h1.life-l1*armor['life'])*price['repair'])))
    print('Helicopter {}:\nprice for refilling ammo: {}\nprice for repairing: {}'.format(num_2,
            (h2.capacity-c2)*price['fill'], round(abs(h2.life-l2*armor['life'])*price['repair'])))

    h1.life = l1 * armor['life']
    h2.life = l2 * armor['life']


def create_helicopters(helicopter_num: int):
    """This function creates helicopters"""

    helicopters = list()

    for i in range(helicopter_num):
        h = Helicopter(speed=random.randint(1, 100), armor=random.randint(1, 100),
                       life=random.randint(1, 100), rapidity=random.randint(1, 100),
                       damage=random.randint(1, 100), capacity=random.randint(1, 100))

        helicopters.append(h)

    return helicopters


def color():
    """This function provides colors for plot"""

    r = random.random()
    b = random.random()
    g = random.random()

    return r, g, b


# number of helicopters
helicopters_num = 10

# parameter of similarity
distance_max = 10

# We create helicopters
helicopters = create_helicopters(helicopters_num)

# We choose battle: 1x1 or all against all
deathmatch = True

# We print all helicopters stats
for i in range(helicopters_num):
    print('========== Helicopter {} stats:'.format(i))
    print_stats(helicopters[i])

# We find integral parameters of helicopters
coords = list()

for i in range(helicopters_num):

    point = (helicopters[i].access_armor(), helicopters[i].access_war())

    coords.append(point)

# We find similarity
dist = distance.cdist(coords, coords, 'euclidean')

print('===== Comparing the helicopters =====\n')

for i in range(helicopters_num):
    for j in range(helicopters_num):

        if i < j:
            if access_similarity(dist[i][j], distance_max):
                print('Helicopters {} and {} are similar'.format(i, j))
            else:
                print('Helicopters {} and {} are different'.format(i, j))

# We plot helicopters transport usability VS war usability
x_list = list()
y_list = list()

for i in range(helicopters_num):

    x_list.append(coords[i][0])
    y_list.append(coords[i][1])

num = 0

fig, ax = plt.subplots()

for x, y in zip(x_list, y_list):

    sc = plt.scatter(x, y, color=color(), label='Helicopter {}'.format(num))
    sr = plt.Circle((x, y), distance_max, color='r', fill=False)
    num += 1

    ax.add_artist(sc)
    ax.add_artist(sr)

plt.axis([0, 100, 0, 100])
plt.xlabel('Armor ratio')
plt.ylabel('War ratio')
plt.legend()
plt.show()


# We play single battle between random helicopters

if not deathmatch:
    while True:
        num_1 = random.randint(0, helicopters_num - 1)
        num_2 = random.randint(0, helicopters_num - 1)

        if num_1 != num_2:
            play_battle(helicopters[num_1], helicopters[num_2], num_1, num_2, repair_rate)
            break

else:
    count_rounds = 0

    while True:

        # We check who survived
        life = list()

        for i in range(helicopters_num):
            life.append(helicopters[i].life)

        count = 0

        for i in life:
            if i > 1:
                count += 1

        # We choose winner
        if count == 1:

            for index, value in enumerate(life):
                if value > 1:
                    count = index
                    break

            print('\n\n\n======= !!!!!! Helicopter {} Wins Deathmatch !!!!! =======\n'.format(count))

            print('Score table:\n')

            for i in range(helicopters_num):
                print('Helicopter {} score: {}'.format(i, helicopters[i].points))

            break

        life.clear()

        while True:
            num_1 = random.randint(0, helicopters_num-1)
            num_2 = random.randint(0, helicopters_num-1)

            if (num_1 != num_2) and (helicopters[num_1].life != 0) and (helicopters[num_2].life != 0):
                count_rounds += 1
                print('\n!!! ROUND {} FIGHT !!! '.format(count_rounds))
                play_battle(helicopters[num_1], helicopters[num_2], num_1, num_2, repair_rate)
                break

