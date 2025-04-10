import copy
import random


class Inventory1:
    inventory = {}

    def get_item(self, item):
        item_found = self.search_item_by_name(item.name)
        if item_found is None:
            item.count = 0
            return item
        else:
            return item_found

    def add_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name].count += item.count
        else:
            self.inventory[item.name] = item

    def delete_item(self, item):
        if item.name in self.inventory:
            if self.inventory[item.name].count > 1:
                self.inventory[item.name].count -= item.count
                if self.inventory[item.name].count <= 0:
                    del self.inventory[item.name]
            else:
                del self.inventory[item.name]
        else:
            print("You don't have this item!!")

    def show_inventory(self):
        for item in self.inventory:
            print(f"{item}: {self.inventory[item].count}")

    def search_item_by_name(self, item):
        for inv_item in self.inventory:
            if inv_item.lower() == item.lower():
                return self.inventory[inv_item]
        return None

class Item:
    def __init__(self, name, count = 1, price = 0, use_message = "You are using this item, but nothing happens", rarity = 0):
        self.name = name
        self.count = count
        self.price = price
        self.use_message = use_message
        self.rarity = rarity

    def use(self, player):
        return self.use_message

    def __str__(self):
        color=rarity_color(self.rarity)
        return color[0] + f"{self.name}: {self.count}" + color[1]

    def __repr__(self):
        color = rarity_color(self.rarity)
        return color[0] + f"{self.name}: {self.count}" + color[1]

def rarity_color(rarity):
    color_start = ""
    color_end = ""
    if rarity == 1:
        color_start = "\x1b[38;5;36m"
        color_end = "\x1b[0m"
    elif rarity == 2:
        color_start = "\x1b[38;5;4m"
        color_end = "\x1b[0m"
    elif rarity == 3:
        color_start = "\x1b[38;5;92m"
        color_end = "\x1b[0m"
    elif rarity == 4:
        color_start = "\x1b[38;5;11m"
        color_end = "\x1b[0m"
    elif rarity == 5:
        color_start = "\x1b[38;5;1m"
        color_end = "\x1b[0m"
    elif rarity == 6:
        color_start = "\x1b[38;5;14m"
        color_end = "\x1b[0m"
    elif rarity == 7:
        color_start = "\x1b[38;5;209m"
        color_end = "\x1b[0m"
    elif rarity == 8:  #HealthPotion
        color_start = "\x1b[38;5;197m"
        color_end = "\x1b[0m"
    elif rarity == 9:  #ManaPotion
        color_start = "\x1b[38;5;75m"
        color_end = "\x1b[0m"
    return [color_start, color_end]


class UsableItem(Item):
    def use(self, player):
        item = copy.deepcopy(self)
        item.count = 1
        player.inventory.delete_item(item)
        return self.use_message


class Coins:
    name = "Coins"
    count = 0
    price = 0

    def __init__(self, count=0):
        self.count = count

    def use(self, player):
        # self.count -= 2 if self.count > 2 else self.count
        player.inventory.delete_item(Coins(random.randint(1, 6)))
        return "You tried to swim in coins, so you threw them into a sewer"

    def __str__(self):
        return f"{self.name}: {self.count}"

    def __repr__(self):
        return f"{self.name}: {self.count}"


class SpellBook(UsableItem):
    def __init__(self, name, count = 1, price = 0, use_message = "You are using this item, but nothing happens", rarity = 0, spells = []):
        super().__init__(name, count, price, use_message, rarity)
        self.spells = spells

    def use(self, player):
        for spell in self.spells:
            if spell not in player.spells:
                player.spells.append(copy.deepcopy(spell))
        return super().use(player) + f"{self.spells}" + f"{player.spells}"


class RandomSpellBook(UsableItem):
    def __init__(self, name, count = 1, price = 0, use_message = "You are using this item, but nothing happens", rarity = 0, spells = []):
        super().__init__(name, count, price, use_message, rarity)
        self.spells = spells

    def use(self, player):
        random_spell = random.choice(self.spells)
        if random_spell not in player.spells:
            player.spells.append(copy.deepcopy(random_spell))
        return super().use(player) + f"{self.spells}" + f"{player.spells}"