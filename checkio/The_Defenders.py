class Warrior(object):
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):
    def __init__(self, attack=7, health=50, defense=0):
        super().__init__(health, attack, defense)

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        super().__init__(health, attack, defense)


def fight(unit_1, unit_2):
    while True:
        if unit_1.attack <= unit_2.defense:
            pass
        else:
            unit_2.health = unit_2.health - (unit_1.attack - unit_2.defense)

        if unit_2.health <= 0:
            return True

        if unit_2.attack <= unit_1.defense:
            pass
        else:
            unit_1.health = unit_1.health - (unit_2.attack - unit_1.defense)

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
                if army_1.s[self.i].attack < army_2.s[self.j].defense:
                    army_2.s[self.j].health = army_2.s[self.j].health
                else:
                    army_2.s[self.j].health = army_2.s[self.j].health - (
                                army_1.s[self.i].attack - army_2.s[self.j].defense)
                # print("self.j:{}".format(army_2.s[self.j].health))
                if army_2.s[self.j].health <= 0:
                    break

                if army_2.s[self.j].attack < army_1.s[self.i].defense:
                    army_1.s[self.i].health = army_1.s[self.i].health
                else:
                    army_1.s[self.i].health = army_1.s[self.i].health - (
                                army_2.s[self.j].attack - army_1.s[self.i].defense)
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

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")