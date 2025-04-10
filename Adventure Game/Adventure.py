import random

from equipment import Helmet, ChestPlate, Boots, Gloves
from invent import Coins, Item, SpellBook
from locatione import Labyrinth, House, Dungeon, Tower, Abandonedfactory
from necronomicon import Coinsrain, HealingSpell, SelfHarm, Blessing
from profile import Player
from mobs import Mob
import copy
from buttons import Menu, Option
from pynput import keyboard
from pynput.keyboard import Key

from shopping import Shop

is_typing = False
current_menu = None

fight_menu = Menu()
global_menu = Menu()
location_menu = Menu()
shop_menu = Menu()
buy_menu = Menu()
sell_menu = Menu()
equipment_menu = Menu()                     #----
necronomicon_menu = Menu()

shop = Shop("Shop")


player = Player(name="Franko", min_damage=0, max_damage=2, hc=4, armor=1, mana=0)
inventory = player.inventory
player.spells = [
    Coinsrain(),
    HealingSpell(),
]

inventory.add_item(Coins(10))
inventory.add_item(Item("Sword", 1, 25))
inventory.add_item(Helmet("Helmet", 1, 1, 1, 4))
inventory.add_item(ChestPlate("ChestPlate", 1, 2, 1, 4))
inventory.add_item(Boots("Boots", 1, 1, 1, 4))
inventory.add_item(Gloves("Gloves", 1, 3, 1, 6))

#####____________\
is_fighting = False
#####____________/
enemy: Mob = None



def adventure(location):
    global enemy
    enemy = copy.deepcopy(location.random_mob())
    enemy.__init__()
    global is_fighting
    is_fighting = True
    player.equipment.reset_all_armor()
    fight_loop()
    print(f"\nYou chose {location.name}")
    print(f"\nYour enemy is: {enemy.name}")


def attack():
    attack_damage = random.randint(player.min_damage, player.max_damage)
    message = enemy.take_damage(attack_damage)
    message2 = enemy_turn()
    message3 = fight_loop()
    print(f"\n" + message)
    if message2 is not None:
        print(message2)
    if message3 is not None:
        print(message3)


def enemy_turn():
    if enemy.hc <= 0:
        global is_fighting
        is_fighting = False
        return
    return enemy.attack(player)


def mercy():
    global is_fighting
    is_fighting = False
    fight_loop()
    print(f"\nYou spared {enemy.name}(ran away)")                         #!!!!!!!!!!!!!!!!


def run_away():
    global is_fighting
    is_fighting = False
    fight_loop()
    print("\nYou decided to chicken out")


def mob_check():
    print(enemy)


def self_check():
    print(player)


def go_to_global_menu():
    change_menu(global_menu)


def change_menu(menu):
    global current_menu
    current_menu = menu
    current_menu.show_options()


def open_inventory(prev_menu = global_menu):
    if len(inventory.inventory) < 0:
        change_menu(prev_menu)
        return
    inventory_menu = Menu()
    inventory_menu.options.clear()
    for item in inventory.inventory:
        option = Option(inventory.inventory[item], lambda itm=item: use_inventory_item(itm, prev_menu))
        inventory_menu.options.append(option)
    change_menu(inventory_menu)
    inventory_menu.options.append(Option(". <", lambda menu=prev_menu: change_menu(menu)))
    current_menu.show_options()


def use_inventory_item(item, menu):
    message = inventory.inventory[item].use(player)
    open_inventory(menu)
    print(message)


def fight_loop():
    print("\nYour options: ")
    global current_menu
    current_menu = fight_menu
    current_menu.show_options()
    if enemy.hc <= 0:
        go_to_global_menu()
        loot = enemy.random_loot()
        items = []
        for item in loot:
            items.append(item())
        for item in items:
            inventory.add_item(copy.deepcopy(item))
        return (f"You defeated {enemy.name}\n"
                f"You received {items}")
    if not is_fighting:
        go_to_global_menu()
    return None


def open_location_menu():
    global current_menu
    current_menu = location_menu
    current_menu.show_options()
    print("\nYou decided to take a walk")


def open_buy_menu():
    if len(shop.shop_items) <= 0:
        go_to_global_menu()
        return
    buy_menu.options.clear()
    for item in shop.shop_items:
        option = Option(f"{item}: {shop.shop_items[item]}", lambda buy_item=item: buy_shop_item(buy_item))
        buy_menu.options.append(option)
    buy_menu.options.append(Option(". <", go_to_global_menu))
    change_menu(buy_menu)


def buy_shop_item(item):
    print(shop.buy_item(item, player))


def open_sell_menu():
    if len(inventory.inventory) <= 0:
        go_to_global_menu()
        return
    sell_menu.options.clear()
    for item in inventory.inventory:
        item = inventory.inventory[item]
        color_start = ""
        color_end = ""
        if item.price <= 0:
            color_start = "\x1b[38;5;8m"
            color_end = "\x1b[0m"
        option = Option(color_start+f"{item.name}: {item.count} - {item.price}"+color_end, lambda sell_item=item: sell_shop_item(sell_item))
        sell_menu.options.append(option)
    sell_menu.options.append(Option(". <", go_to_global_menu))
    change_menu(sell_menu)


def sell_shop_item(item):
    message = shop.sell_item(item, player)
    open_sell_menu()
    print(message)


def open_equipment_menu():
    equipment_menu.options.clear()
    for equipment_type in player.equipment.slots:
        option = Option(equipment_type, lambda name=equipment_type: open_equipment_type_inventory(name))
        equipment_menu.options.append(option)
    equipment_menu.options.append(Option(". <", go_to_global_menu))
    change_menu(equipment_menu)


def open_equipment_type_inventory(name):
    equipment_type_menu = Menu()
    equipment_type_menu.options.clear()
    for item in inventory.inventory:
        item = inventory.inventory[item]
        color_start = ""
        color_end = ""
        if type(item).__name__!=name:
            color_start = "\x1b[38;5;8m"
            color_end = "\x1b[0m"
            option = Option(color_start + f"{item.name}: {item.count} - {type(item).__name__}" + color_end, lambda: print("hui"))
            equipment_type_menu.options.append(option)
            continue
        option = Option(f"{item.name}: {item.count} - {type(item).__name__}", lambda equip_item=item: player.equipment.equip(equip_item))
        equipment_type_menu.options.append(option)
    equipment_type_menu.options.append(Option(". <", open_equipment_menu))
    change_menu(equipment_type_menu)


def open_necronomicon_menu(prev_menu = global_menu):
    necronomicon_menu.options.clear()
    for spell in player.spells:
        option = Option(f"{spell}: {spell.required_mana}", lambda usa_spell=spell: use_spell(usa_spell))
        necronomicon_menu.options.append(option)
    necronomicon_menu.options.append(Option(". <", lambda menu=prev_menu:change_menu(menu)))
    change_menu(necronomicon_menu)

def use_spell(spell):
    print(spell.use_spell(player))
    # print(necronomicon.Coinsrain.use_spell(spell, player))



location_menu.options = [
    Option("Labyrinth", lambda loc=Labyrinth(): adventure(loc)),
    Option("House", lambda loc=House(): adventure(loc)),
    Option("Dungeon", lambda loc=Dungeon(): adventure(loc)),
    Option("Tower", lambda loc=Tower(): adventure(loc)),
    Option("Abandoned Factory", lambda loc=Abandonedfactory(): adventure(loc)),
    Option(". <", go_to_global_menu),
]


global_menu.options = [
    Option("Go For a Walk", open_location_menu),
    Option("Open Inventory", lambda menu=global_menu: open_inventory(menu)),
    Option("Profile", self_check),
    Option("Shop", lambda menu=shop_menu: change_menu(menu)),
    Option("Necronomicon", open_necronomicon_menu),       #----
    Option("Equipment", open_equipment_menu),
    Option("Exit", exit)
]


fight_menu.options = [
    Option("Attack", attack),
    Option("Mercy", mercy),
    Option("Run Away", run_away),
    Option("Open Inventory", lambda menu=fight_menu: open_inventory(menu)),
    Option("Necronomicon", lambda menu=fight_menu: open_necronomicon_menu(menu)),       #----
    Option("Mob Check", mob_check),
    Option("Profile", self_check),
]



shop_menu.options = [
    Option("Buy", open_buy_menu),
    Option("Sell", open_sell_menu),
    Option(". <", go_to_global_menu),
]



necronomicon_menu.options = [                                                               #---->
    Option("Use Spell", open_necronomicon_menu),                                        #---->
    Option("Learn Spell", lambda menu=necronomicon_menu: change_menu(menu)),            #---->
    Option(". <", go_to_global_menu),                                                   #---->
]                                                                                           #---->

go_to_global_menu()


def on_key_release(key):
    if key == Key.down:
        current_menu.move_down()
        current_menu.show_options()
    elif key == Key.up:
        current_menu.move_up()
        current_menu.show_options()
    elif key == Key.enter:
        current_menu.interact()


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()