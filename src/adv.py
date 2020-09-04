from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'eastColony': Room("East Colony", """Get a shovel to dig a tunnel to north or
go west."""),

    'dungeon': Room("Dungeon", """Find the lamp so that u can find the treasure and
way out."""),

    'secretTunnel': Room("Secret Tunnel", """You are almost there, get the treasure or
you'll loose it to others.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['eastColony'].e_to = room['foyer']
room['foyer'].w_to = room['eastColony']
room['dungeon'].s_to = room['overlook']
room['overlook'].n_to = room['dungeon']
room['secretTunnel'].w_to = room['dungeon']
room['dungeon'].e_to = room['secretTunnel']
room['secretTunnel'].s_to = room['treasure']
room['treasure'].n_to = room['secretTunnel']

#
# Add some items to each room
#
item1 = Item('sword', 'Ex-caliber of King Arthur')
item2 = Item('armor', 'Suite to save')
item3 = Item('shovel', 'Long and sharp')
item4 = Item('arrows', 'Poisonous')
item5 = Item('rope', 'A long and thick rope')

treasure1 = Treasure('diamond', 'Blue nile', 100)
treasure2 = Treasure('gold', 'A coin from 3000BC', 50)
treasure3 = Treasure('sapphires', 'Shiny and precious', 10)

lightSource1 = LightSource('super bright', 'sun')
lightSource2 = LightSource('bright', 'lamp')
lightSource3 = LightSource('dull', 'candles and matchstick', 'Found it')
lightSource4 = LightSource('dim', 'flaming torch light', 'Light it')

# room['outside'].add_item(item1)
# room['outside'].add_item(lightSource1)
# room['outside'].is_light = True
room['outside'].add_item(item1).add_item(lightSource1).is_light = True
room['outside'].add_item(item2)
room['foyer'].items.append(lightSource2)
room['foyer'].is_light = True
room['eastColony'].add_item(item3)
room['eastColony'].items.append(lightSource3)
room['overlook'].add_item(item4)
room['overlook'].items.append(lightSource3)
room['dungeon'].add_item(item1)
room['dungeon'].items.append(lightSource4)


# player.items = [item5, item6, item7]
# player.current_room.items = [item1, item2, item3, item4]
def get_lightSource(player):
    for item in player.current_room.items:
        if isinstance(item, LightSource):
            return item

    for item in player.items:
        if isinstance(item, LightSource):
            return item

    return None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = {
#     'name': 'Jack',
#     'player.player.current_room': ''
# }


john = Player('John', room['outside'])
judy = Player('Judy', room['foyer'])
# Write a loop that:
move = ''
player_name = input('Select a player: (John or Judy)')

if player_name == 'John':
    player = john
else:
    player = judy

while True:
    print('')
    print('************')
    print('Current room: ', player.current_room.name)
    print('Description: ', player.current_room.description)
    light_source = get_lightSource(player)
    if light_source:
        print('Light:', light_source.name)
        print('Light description: ', light_source.description)
    else:
        print('Its pitch dark in here!')
    # print('Score:', player.current_room.is_score)

    move = input('Please enter the command:')

    try:
        # inventory list
        if move in ['i', 'inventory']:
            print('************')
            print('Inventory:')
            for item in player.items:
                print(item)
            for treasure in player.bag:
                print(treasure)
            print('************')
            continue
        # what item player has in the room
        elif move in ['l', 'list']:
            print('************')
            print('List:')
            for item in player.current_room.items:
                print(item)
            print('************')
            continue
        # player takes/gets the item/weapon and finds the treasure
        elif move.split()[0] in ['get', 'take']:
            # import pdb;
            # pdb.set_trace()
            item_name = move.split()[1]
            treasure_name = move.split()[1]
            found_item = False
            for item in player.current_room.items:
                if item_name == item.name:
                    item.on_take()
                    if isinstance(item, Treasure):
                        player.bag.append(item)
                    else:
                        player.items.append(item)
                    player.current_room.items.remove(item)
                    found_item = True
                    break
            if not found_item:
                print('The item is not in the current room')
            # player drops the item/weapon      
        elif move.split()[0] == 'drop':
            item_name = move.split()[1]
            for item in player.items + player.bag:
                if isinstance(item, Treasure):
                    print('Hold onto it')
                    continue
                if isinstance(item, Item):
                    if item_name == item.name:
                        player.items.remove(item)
                        player.current_room.items.append(item)
                        item.on_drop()
                        break
                else:
                    print("The item is not with player")
        elif move in ['n', 'north']:
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                # if player.current_room.is_light():
                #     print(f'There is light source:
                #         {player.current_room.light.name}')
                # else:
                #     print("It's pitch black!")    
            else:
                print('There is no room to the north of current room: {}'
                ''.format(player.current_room.name))
            continue
        elif move == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print('There is no room to the east of current room: {}'
                ''.format(player.current_room.name))
            continue
        elif move == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print('There is no room to the south of current room: {}'
                ''.format(player.current_room.name))
            continue
        elif move == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print('There is no room to the west of current room: {}'
                ''.format(player.current_room.name))
            continue
        elif move == 'q':
            print('Quitting')
            break
    except ValueError:
        print('The player is in wrong room.')
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game. 
