from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    
    num_move = 0
    
    while not PLAYER.victory and num_move < 20:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        #   print either full description (first time visit) or brief description (every subsequent visit)
        if (PLAYER.visit_location(location)):
            print(location.brief)
        else:
            PLAYER.score += location.point
            print(location.long)

        print("\nWhat to do? \n")
        for action in location.available_actions(WORLD, PLAYER):
            print(action)
        choice = input("Enter action: ")
        if choice in ["south", "north", "east", "west"]:
            if ("south" in choice):
                PLAYER.move_south()
            if ("north" in choice):
                PLAYER.move_north()
            if ("east" in choice):
                PLAYER.move_east()
            if ("west" in choice):
                PLAYER.move_west()
            num_move += 1
        if "take" in choice:
            choice = choice.split()
            name = " ".join(choice[1:])
            PLAYER.inventory.append(location.items[name])
            del location.items[name]
        if "deposit" in choice:
            choice = choice.split()
            name = " ".join(choice[1:])
            for item in PLAYER.inventory:
                if item.name == choice:
                    PLAYER.remove_item(item)
                    location.items[item.name] = item
        
        if choice == "look":
            print(location.long)
        if choice == "inventory":
            for item in PLAYER.get_inventory():
                print(item.name)
        if choice == "score":
            print("Current Score: " + str(PLAYER.score))
        if choice == "quit":
            print("You quit the game")
            break
            

        # CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON USER'S CHOICE
        #    REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if the
        #               choice the user made was just a movement, so only updating player's position is enough to change
        #               the location to the next appropriate location
        # Possibilities: a helper function do_action(WORLD, PLAYER, location, choice)
        # OR A method in World class WORLD.do_action(PLAYER, location, choice)
        # OR Check what type of action it is, then modify only player or location accordingly
        # OR Method in Player class for move or updating inventory
        # OR Method in Location class for updating location item info, or other location data
        # etc....
