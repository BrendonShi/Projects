import random

from invent import Item, Coins, UsableItem, SpellBook, RandomSpellBook
from classpotion import HealthPotion, ManaPotion
from necronomicon import SelfHarm, Coinsrain, Blessing
from utils import progress_bar


class Mob:
    def __init__(self, name, hc, min_damage, max_damage):
        self.name = name
        self.hc = hc
        self.max_hc = hc
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.loot_amount = 1
        self.loot_table = {
            lambda: Coins(10): 0.45,
            lambda: HealthPotion(1): 0.2,
            lambda: ManaPotion(1): 0.2,
            lambda: Item("Carrot", 1): 0.1,
            lambda: Item("Iron Sword", 1): 0.05,
        }


    def __str__(self):
        return f"\n{self.name}'s stats is: \nHC: {progress_bar(self.hc, self.max_hc)}, \nDamage: {self.min_damage}-{self.max_damage}"


    def random_loot(self):
        items = list(self.loot_table.keys())
        chances = list(self.loot_table.values())
        return random.choices(items, weights = chances, k = self.loot_amount)


    def attack(self, player):
        attack_damage = random.randint(self.min_damage, self.max_damage)
        return player.take_damage(attack_damage)


    def take_damage(self, damage):
        self.hc -= damage
        return f"{self.name} took {damage} damage!"


class Zombie(Mob):
    def __init__(self):
        super().__init__("Zombie", 2, 0, 2)
        self.loot_table = {
            lambda: Coins(random.randint(1, 10)): 0.3,
            lambda: HealthPotion(1): 0.2,
            lambda: ManaPotion(1): 0.2,
            lambda: Item("Carrot", 1, 5): 0.1,
            lambda: Item("Iron Sword", 1, 7, rarity=1): 0.15,
            lambda: Item("Rotten Potato", 1, 25, rarity=3): 0.05
        }



class Skeleton(Mob):
    def __init__(self):
        super().__init__("Skeleton", 1, 1, 1)
        self.loot_table = {
            lambda: Coins(random.randint(1, 7)): 0.3,
            lambda: HealthPotion(1): 0.1,
            lambda: ManaPotion(1): 0.1,
            lambda: Item("Broken Bone", 1, 2): 0.2,
            lambda: Item("Bow", 1, 20, rarity=2): 0.05,
            lambda: Item("Damaged Bow", 1, 12, rarity=1): 0.15,
            lambda: UsableItem("Garlic", 1, 2, rarity=1, use_message="You took a bite of garlic, you're now seasoned, as any good meal should be. (Vampires will appreciate it)"): 0.99,
            lambda: Item("Damaged Broken Bone-Bow", 1, 60, rarity=4): 0.01,
        }


class Werewolf(Mob):
    def __init__(self):
        super().__init__("Werewolf", 4, 1, 4)
        self.loot_amount = random.randint(2, 3)
        self.loot_table = {
            lambda: Coins(random.randint(10, 20)): 0.3,
            lambda: HealthPotion(1): 0.2,
            lambda: ManaPotion(1): 0.2,
            lambda: Item("Wolf Tail", 1, 90, rarity=3): 0.03,
            lambda: Item("Wolf Hide", 1, 85, rarity=3): 0.04,
            lambda: Item("Wolf Broken Bone", 1, 80, rarity=2): 0.05,
            lambda: Item("Wolf Fang", 1, 75, rarity=2): 0.06,
            lambda: Item("Werewolf Eye", 1, 160, rarity=5): 0.01,
            lambda: Item("Monster Blood", 1, 140, rarity=5): 0.02,
            lambda: Item("Werewolf Head", 1, 340, rarity=6): 0.005,
            lambda: Item("Moonstone Ring", 1, 400,rarity=6): 0.005,
            lambda: Item("Elden Ring", 1, 500, rarity=7): 0.001,
            lambda: Item("Scimitar", 1, 15, rarity=2): 0.079,
        }


class Slime(Mob):
    def __init__(self):
        super().__init__("Slime", 1, 0, 1)
        self.loot_table = {
            lambda: Coins(random.randint(1, 5)): 0.3,
            lambda: HealthPotion(1): 0.2,
            lambda: ManaPotion(1): 0.2,
            lambda: Item("Green Goo", random.randint(1, 3), 1, rarity=1): 0.2,
            lambda: Item("Satoru Gojo's Figure", 1, 500, "You looked at the figure... and now world feels so... so wonderful right now.", 7): 0.001,
            lambda: Item("Enchanted Broken Finger", 1, 270, rarity=5): 0.01,
            lambda: Item("Cursed Dark Glove?", 1, 220, rarity=5): 0.01,
            lambda: Item("Broken Magic Mirror", 1, 75, rarity=3): 0.049,
            lambda: Item("Recovered Kitchen Fork", 1, 40, rarity=2): 0.03,
        }


class Survivor(Mob):
    def __init__(self):
        super().__init__("Survivor", 2, 1, 3)
        self.loot_table = {
            lambda: Coins(random.randint(3, 12)): 0.3,
            lambda: HealthPotion(1): 0.2,
            lambda: ManaPotion(1): 0.2,
            lambda: Item("Leather Helmet", 1, 20, rarity=1): 0.05,
            lambda: Item("Leather Black Gloves", 1, 20, rarity=1): 0.05,
            lambda: Item("Barrel Of Shotgun", 1, 25, rarity=2): 0.05,
            lambda: Item("Photo Of Survivor", 1, 300, rarity=5): 0.01,
            lambda: Item("Ember Necklace", 1, 170, rarity=4): 0.04,
            lambda: Item("Moonstone Ring", 1, 400, rarity=6): 0.005,
            lambda: Item("Slave Chain", random.randint(1, 3), 90, rarity=3): 0.05,
            lambda: Item("Totem Of Beast's Breasts", 1, 140, rarity=4): 0.045
        }


class Shadowthing(Mob):
    def __init__(self):
        super().__init__("Shadow Thing", 5, 4, 5)
        self.loot_amount = random.randint(2, 4)
        self.loot_table = {
            lambda: Coins(random.randint(20, 40)): 0.3,
            lambda: HealthPotion(random.randint(1, 3)): 0.2,
            lambda: ManaPotion(random.randint(1, 3)): 0.2,
            lambda: Item("Dragonborn Embrione", 1, 240, rarity=5): 0.04,
            lambda: Item("Book Of Shadows", 1, 260, rarity=5): 0.05,     # spellbook
            lambda: RandomSpellBook("Paper Of Light", 1, 431, rarity=6, spells=[Blessing()]): 0.05,
            lambda: Item("Eye Of Darkness", 1, 264, rarity=5): 0.05,
            lambda: Item("Heart Of Void", 1, 200, rarity=4): 0.05,
            lambda: Item("Dark Matter", random.randint(1, 3), 180, rarity=4): 0.05,
            lambda: Item("Cursed Enchanted Rotten Broken Damaged Bone", 1, 460, rarity=7): 0.01,
        }


# class Mermaid(Mob):
# class Unicorn(Mob):
# class Gnome(Mob):

# Make a special loot for each mob