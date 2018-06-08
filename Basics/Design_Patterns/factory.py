from random import randrange


class Weapon():
    name = None
    cost = None

    @staticmethod
    def get_weapon(x):
        if x == 0:
            return Knife()
        if x == 1:
            return Gun()


class Knife(Weapon):
    name = 'Knife'
    cost = 20.00


class Gun(Weapon):
    name = 'Gun'
    cost = 300.00


for _ in range(25):
    w = Weapon.get_weapon(randrange(2))
    print(w.name, w.cost)
