import random
from invent import Coins


class Spell:
    def __init__(self, name, effect, required_mana):
        self.name = name
        self.effect = effect
        self.required_mana = required_mana

    def print_spell_info(self):
        print(f"Spell: {self.name}")
        print(f"Effect: {self.effect}")
        print(f"Mana required: {self.required_mana}")

    def use_spell(self, player):
        if not self.consume_mana(player):
            return "Not enough mama!"

    def consume_mana(self, player):
        if player.mana >= self.required_mana:
            player.mana -= self.required_mana
            return True
        return False

    # def learn_spell(self, player):
    #     player.spells.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Coinsrain(Spell):
    def __init__(self):
        super().__init__("Coinsrain", "Wow, coinss...", 120)

    def use_spell(self, player):
        if not super().consume_mana(player):
            return "Not enough mama!"
        randomcoins = random.randint(25, 80) #S
        player.inventory.add_item(Coins(randomcoins)) #S
        return f"You've cast a spell! Out of nowhere, coins started falling right above the head, it doesn't look like a rain of coins... You received: {randomcoins}"


class HealingSpell(Spell):
    def __init__(self):
        super().__init__("Healing Spell", "Heals 1 health chunk", 50)

    def use_spell(self, player):
        if player.hc >= 4:
            return "Your HC is full, nigga!!!"
        if not super().consume_mana(player):
            return "Not enough mama!"
        player.hc += 1
        return f"You've restored 1 health chunk! Now your HC: {player.hc}"


class SelfHarm(Spell):
    def __init__(self):
        super().__init__("Self Harm Spell", "Gives you money", 20)

    def use_spell(self, player):
        if not super().consume_mana(player):
            return "Not enough mama!"
        player.take_damage(1)
        player.inventory.add_item(Coins(10))
        return f"You lost 1 HC and received 10 coins"


class Blessing(Spell):
    def __init__(self):
        super().__init__("Blessing", "", 200)

    def use_spell(self, player):
        if not super().consume_mana(player):
            return "Not enough mama!"
        player.hc += 8
        return "You have got a blessing, now you feel like something warming your heart, it's the best feeling that you've ever felt"

