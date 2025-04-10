from invent import rarity_color


class Potions:
    price = 0
    rarity = 0
    def __init__(self, name, effect, count):
        self.name = name
        self.effect = effect
        self.count = count

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Effect: {self.effect}")
        print(f"Count: {self.count}")

    def use(self, player):
        pass

    def __str__(self):
        color = rarity_color(self.rarity)
        return color[0] + f"{self.name}: {self.count}" + color[1]

    def __repr__(self):
        color = rarity_color(self.rarity)
        return color[0] + f"{self.name}: {self.count}" + color[1]


class HealthPotion(Potions):
    rarity = 8
    def __init__(self, count):
        super().__init__("Health Potion", "Heal 1 health chunk!", count)

    def use(self, player):
        if player.hc < 4 and self.count > 0:
            player.hc += 1
            player.inventory.delete_item(HealthPotion(1))
            return f"You used a {self.name} and healed 1 hc! Your current health is {player.hc}"
        else:
            return "Your health is full!!"

class ManaPotion(Potions):
    rarity = 9
    def __init__(self, count):
        super().__init__("Mana Potion", "Restore 20 mana!", count)

    def use(self, player):
        if player.mana < 200 and self.count > 0:
            player.mana += 20
            player.inventory.delete_item(ManaPotion(1))
            return f"You used a {self.name} and restored 20 mana! Your current mana is {player.mana}"
        else:
            return "Your mama is full!!"
