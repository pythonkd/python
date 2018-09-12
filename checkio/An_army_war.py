class Warrior(object):
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):
    def __init__(self, attack=7, health=50):
        super().__init__(health, attack)

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            return True

        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            return False


class Army(object):
    def __init__(self):
        self.s = []

    def add_units(self, fclass, n):
        for i in range(n):
            self.s.append(fclass())


class Battle(object):
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

    def fight(self, army_1, army_2):

        while army_1.s[-1].health > 0:
            while True:
                army_2.s[self.j].health -= army_1.s[self.i].attack
                # print("self.j:{}".format(army_2.s[self.j].health))
                if army_2.s[self.j].health <= 0:
                    break
                army_1.s[self.i].health -= army_2.s[self.j].attack
                # print("self.i:{}".format(army_1.s[self.j].health))
                if army_1.s[self.i].health <= 0:
                    break

            if army_2.s[-1].health <= 0:
                return True
            if army_1.s[-1].health <= 0:
                return False
            if army_1.s[self.i].health <= 0:
                self.i += 1
            elif army_2.s[self.j].health <= 0:
                self.j += 1
            # print(self.i, self.j)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")