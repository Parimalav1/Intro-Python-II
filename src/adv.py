from room import Room
from player import Player
from item import Item

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

#
# Add some items to each room
#
item1 = Item('sword', 'Ex-caliber of King Arthur')
item2 = Item('diamond', 'Blue nile')
item3 = Item('gold', 'A coin from 3000BC')

room['outside'].add_item(item1)
room['outside'].add_item(item2)
room['outside'].add_item(item3)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = {
#     'name': 'Jack',
#     'player.player.current_room': ''
# }
player = Player('John', room['outside'])
# Write a loop that:
move = ''
while True:
    print('')
    print('************')
    print('Current room: ', player.current_room.name)
    print('Description: ', player.current_room.description)

    move = input('Please enter the command:')

    try:
        if move in ['i', 'inventory']:
            print('************')
            print('Inventory:')
            for item in player.items:
                print(item)
            print('************')
            continue
        elif move in ['l', 'list']:
            print('************')
            print('List:')
            for item in player.current_room.items:
                print(item)
            print('************')
            continue
        elif move.split()[0] in ['get', 'take']:
            # import pdb;
            # pdb.set_trace()
            item_name = move.split()[1]
            for item in player.current_room.items:
                if item_name == item.name:
                    item.on_take()
                    player.items.append(item)
                    player.current_room.items.remove(item)
                    break
                else:
                    print('The item is not in the current room')
        elif move.split()[0] == 'drop':
            item_name = move.split()[1]
            for item in player.items:
                if item_name == item.name:
                    player.items.remove(item)
                    player.current_room.items.append(item)
                    item.on_drop()
                    break
                else:
                    print("The item is not in the player's bag")
        elif move in ['n', 'north']:
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
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
