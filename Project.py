import math

def show_instructions():

    print("Giant Wolf Game")
    print()
    print("Collect all 8 items to defeat the wolf.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("To exit the game: 'Exit'")
    print("------------------------------")

def show_status():

    print("You are in the {}".format(current_room))
    print('Inventory: ', inventory)
    print("------------------------------")

    current_dict = rooms[current_room]
    item = 'None'
    if 'item' in current_dict:
        item = current_dict['item']
        print('You see a', item)


rooms = {
    'Living room': {'South': 'Bedroom one', 'North': 'Garage', 'East': 'Basement',
                   'West': 'Library', 'item': 'Flashlight'},
    'Bedroom one': {'North': 'Living room', 'East': 'Bedroom two', 'item': 'Silver Bullet'},
    'Bedroom two': {'West': 'Bedroom one', 'item': 'Silver Gun'},
    'Bedroom three': {'South': 'Basement', 'item': 'Silver Dagger', "East" : "backyard"},

    'Basement': {'West':'Living room', 'North': 'Bedroom three', 'item': 'Armor'},
    'Garage' : {'South':'Living room',"West" : "Attic",'item': 'Magic Drink'},
    'Library': {'East':'Living room',"North" : "Attic", 'item': 'Spell Book'},
    'Attic': {'South':'Library', 'item': 'Shield',"East" : "Garage"},
    'backyard': {'East':'Bedroom three', 'item': 'The Wolf'}
}


inventory = []

starting_room = 'Living room'

current_room = starting_room


show_instructions()

while True:
    show_status()
    if current_room == 'backyard':
        if len(inventory) == 8:
                for i in range(1000000):
                    j = math.sin(i / 2000000)
                    if i % 100000 == 0:
                        print("Fighting the Giant wolf...")
                print("Congratulations! You have killed the Giant wolf.")
        else:
            print("You have been killed!")
        print('Thanks for playing!')
        break
    word_list = input("Enter your move: ").split()
    print()
    word_list = [x.capitalize() for x in word_list]
    if len(word_list) == 1:
        if word_list[0] == "Exit":
            current_room = 'exit'
            print('------------------------------')
            print('Thanks for playing! Hope you enjoyed it!')
            break
        else:
            print('Inva1id Input!')
            continue
    elif len(word_list) >= 2:
        action = word_list[0]
        if action == "Go":
            if len(word_list) > 2:
                print('Invalid Input!')
                continue
            direction = word_list[1]
            possible_rooms = rooms[current_room]
            if direction in possible_rooms:
                current_room = possible_rooms[direction]
            else:
                print(f'Invalid Input!')
        elif action == "Get":
            if 'item' in rooms[current_room]:
                item_name = ''
                i = 1
                for val in word_list[1:]:
                    if i != 1:
                        item_name += f' {val}'
                        print(item_name, 'retrieved!')
                        print()
                    else:
                        item_name += val
                    i += 1
                if rooms[current_room]["item"] == item_name:
                    inventory.append(item_name)
                    rooms[current_room].pop("item")
                    if len(inventory) == 8:
                        print(
                            "You have collected all 8 items! Go find and kill giant wolf")
                else:
                    print("Invalid Input!")
            else:
                print("Invalid Input!")
        else:
            print('Cannot get that item!')
