import random

from mobs import Zombie, Werewolf, Skeleton, Survivor, Shadowthing, Slime, Mob


mobs = [
    Zombie(),
    Skeleton(),
    Werewolf(),
    Slime(),
    Survivor(),
    Shadowthing()
]


class Location:
    def __init__(self, name, mobs: list[Mob]):
        self.name = name
        self.mobs = mobs


    def print_location(self):
        print(f"Location: {self.name}")
        print(f"Mobs: {self.mobs}")
        for mob in self.mobs:
            mob.print()


    def random_mob(self):
        return random.choice(self.mobs)


class Labyrinth(Location):
    def __init__(self):
        super().__init__("Labyrinth", [Slime()])


class House(Location):
    def __init__(self):
        super().__init__("House", [Zombie(), Survivor(), Werewolf()])


class Dungeon(Location):
    def __init__(self):
        super().__init__("Dungeon", [Zombie(), Skeleton(), Slime()])


class Tower(Location):
    def __init__(self):
        super().__init__("Tower", [Zombie(), Survivor()])


class Abandonedfactory(Location):
    def __init__(self):
        super().__init__("Abandoned Factory", [Werewolf(), Shadowthing(), Slime(), Survivor(), Zombie(), Skeleton()])


# class Swamp(Location):
# class Meadow(Location):
# class Mine(Location):