from equipment import EquipmentManager
from invent import Inventory1
from utils import progress_bar


class Player:
    inventory = None
    spells = []
    def __init__(self, name, min_damage, max_damage, armor, hc, mana):
        self.inventory = Inventory1()
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.armor = armor
        self.hc = hc
        self.mana = mana
        self.equipment = EquipmentManager()


    def __str__(self):
        return f"\n{self.name}'s profile is: \nHC: {progress_bar(self.hc, 4)}, \nMana: {self.mana}, \nEquipment: {self.equipment},\nDamage: {self.min_damage}-{self.max_damage},\nArmor: {self.armor}"


    def take_damage(self, damage):
        hp_damage, slot = self.equipment.take_armor_damage(damage)
        self.hc -= hp_damage
        if self.hc <= 0:
            print("Game over!")
            exit()

        return f"{self.name} took {damage} damage in {slot.name}!"



    # def print_info(self):
    #     print (f"\n{self.name}'s profile:")
    #     print (f"Equipment: {self.equipment}")
    #     print (f"Damage: {self.min_damage}-{self.max_damage}")
    #     print (f"HC: {self.hc}")
    #     print (f"Mana: {self.mana}")
    #     print (f"Armor: {self.armor}")