import copy

from classpotion import HealthPotion, ManaPotion
from equipment import Armor
from invent import Coins


class Shop:
    shop_items = {
        HealthPotion(1): 10,
        ManaPotion(1): 10,
    }
    def __init__(self, name):
        self.name = name


    def buy_item(self, item, player):
        coins = player.inventory.search_item_by_name("Coins")
        if coins is None:
            return "\nNot enough money!!"
        if item in self.shop_items and self.shop_items[item] <= coins.count:
            player.inventory.delete_item(Coins(self.shop_items[item]))
            item = copy.deepcopy(item)
            player.inventory.add_item(item)
            return f"\nYou bought {item.name}. Your current coins {coins.count}"
        else:
            return "\nNot enough money!!"


    def sell_item(self, item, player):
        if item.price > 0:
            del_item = copy.deepcopy(item)
            del_item.count = 1
            # kostyl'                                                                         !!!!!!!!!
            if isinstance(item, Armor):
                if player.equipment.is_equipped(item):
                    player.equipment.unequip(item.slot_type)
            player.inventory.delete_item(del_item)
            player.inventory.add_item(Coins(item.price))
            coins = player.inventory.search_item_by_name("Coins")
            coins_amount = 0
            if coins is not None:
                coins_amount = coins.count
            return f"\nYou sold {item.name}. Your current coins {coins_amount}"
        else:
            return "\nI'd rather buy your mama than this shit."