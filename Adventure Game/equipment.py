import random


class Armor:
    def __init__(self, name, count, max_armor, price, durability):
        self.name = name
        self.count = count
        self.max_armor = max_armor
        self.__armor = max_armor
        self.price = price
        self.slot_type = ""
        self.__durability = durability
        self.broken = False

    def get_armor(self):
        return self.__armor

    def get_durability(self):
        return self.__durability

    def take_durability_damage(self, damage):
        if self.__armor <= 0:
            return
        damage = damage if damage <= self.max_armor else self.max_armor
        self.__durability -= damage
        if self.__durability <= 0:
            self.__durability = 0
            self.broken = True

    def take_armor_damage(self, damage):
        damage2 = damage - self.__armor
        self.take_durability_damage(damage)
        self.__armor -= damage
        if self.__armor <= 0:
            self.__armor = 0
        return damage2 if damage2 >= 0 else 0

    def reset_armor(self):
        self.__armor = self.max_armor if self.__durability >= self.max_armor else self.__durability

    def use(self, player):
        return "Mmmmmmmm.... shiny!"

    def __str__(self):
        return f"{self.name} - {self.__armor}: {self.__durability}"

    def __repr__(self):
        return f"{self.name} - {self.__armor}: {self.__durability}"


class Helmet(Armor):
    def __init__(self, name, count, armor, price, durability):
        super().__init__(name, count, armor, price, durability)
        self.slot_type = "Helmet"


class ChestPlate(Armor):
    def __init__(self, name, count, armor, price, durability):
        super().__init__(name, count, armor, price, durability)
        self.slot_type = "ChestPlate"


class Boots(Armor):
    def __init__(self, name, count, armor, price, durability):
        super().__init__(name, count, armor, price, durability)
        self.slot_type = "Boots"


class Gloves(Armor):
    def __init__(self, name, count, armor, price, durability):
        super().__init__(name, count, armor, price, durability)
        self.slot_type = "Gloves"

    def use(self, player):
        return "Gloves"


class EquipmentManager:
    def __init__(self):
        self.slots = {
            "Helmet": EquipmentSlot("Helmet"),
            "ChestPlate": EquipmentSlot("ChestPlate"),
            "Boots": EquipmentSlot("Boots"),
            "Gloves": EquipmentSlot("Gloves"),
        }

    def equip(self, item):
        if item.slot_type in self.slots:
            self.slots[item.slot_type].equip(item)

    def unequip(self, slot):
        if slot in self.slots:
            self.slots[slot].unequip()

    def is_equipped(self, item):
        is_found = False
        for slot in self.slots:
            if self.slots[slot].get_item() == item:
                is_found = True
                break
        return is_found

    def get_random_slot(self):
        return random.choice(list(self.slots.values()))

    def take_armor_damage(self, damage):
        slot = self.get_random_slot()
        if slot.is_empty():
            return damage, slot
        return slot.take_armor_damage(damage), slot

    def reset_all_armor(self):
        for slot in self.slots:
            self.slots[slot].reset_armor()

    def calculate_defense(self):
        defense = 0
        for slot in self.slots:
            defense += self.slots[slot].get_defense()
        return defense

    def __str__(self):
        return f"{list(self.slots.values())}"


class EquipmentSlot:
    def __init__(self, name):
        self.name = name
        self.__item = None

    def equip(self, item):
        self.__item = item

    def unequip(self):
        self.__item = None

    def get_defense(self):
        if self.__item is None:
            return 0
        return self.__item.get_armor()

    def get_item(self):
        return self.__item

    def is_empty(self):
        return self.__item is None

    def take_armor_damage(self, damage):
        if self.__item is None:
            return
        return self.__item.take_armor_damage(damage)

    def reset_armor(self):
        if self.__item is None:
            return
        self.__item.reset_armor()

    def __str__(self):
        if self.__item is not None:
            return f"{self.__item}"
        return f""

    def __repr__(self):
        if self.__item is not None:
            return f"{self.__item}"
        return f""