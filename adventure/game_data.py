class Location:

    def __init__(self, position, point, brief, long):
        '''Creates a new location.

        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''
        self.position = position
        self.point = point
        self.brief = brief
        self.long = long
        self.items = {}

    def get_brief_description (self):
        '''Return str brief description of location.'''
        return self.brief

    def get_full_description (self):
        '''Return str long description of location.'''
        return self.long

    def available_actions(self, world, player):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.'''
        
        actions = ["look", "inventory", "score", "quit"]
        map_size = len(world.map)
        for i in range(map_size):
            if self.position in world.map[i]:
                position_y = i
                position_x = world.map[i].index(self.position)
        if (position_y - 1 >= 0 and world.map[position_y - 1][position_x] != -1):
            actions.append("north")
        if (position_y + 1 < map_size  and world.map[position_y + 1][position_x] != -1):
            actions.append("south")
        if (position_x + 1 < map_size  and world.map[position_y][position_x + 1] != -1):
            actions.append("east")
        if (position_x - 1 >= 0  and world.map[position_y][position_x - 1] != -1):
            actions.append("west")
        for name in self.items:
            actions.append("take " + name)
        for item in player.inventory:
            if item.target == self.position:
                actions.append("deposit " + item.name)
        return actions

class Item:

    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def __str__(self):
        return "Name: " + self.name + '/n' + "Start: " + str(self.start) + '/n' + "Target: " + str(self.target) + '/n' + "Target Points: " + str(self.target_points)

    def get_starting_location (self):
        '''Return int location where item is first found.'''

        return self.start

    def get_name(self):
        '''Return the str name of the item.'''

        return self.name

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''

        return self.target

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''

        return self.target_points

class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.items = self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.locations = self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of integers like so:
            1 2 5
            3 -1 4
        becomes [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of integers representing map of game world as specified above
        '''
        map_list = []
        map_file = open(filename, "r")
        for line in map_file:
            row = []
            int_list = line.strip().split()
            for num in int_list:
                row.append(int(num))
            map_list.append(row)
        return map_list


    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return:
        '''

        locations = {}
        location_file = open(filename, "r")
        location_list = []
        for line in location_file:
            line = line.strip()
            if (len(line) > 0):
                if ("LOCATION" in line):
                    line = int(line.split()[-1])
                elif (len(line) == 1):
                    line = int(line)
                location_list.append(line)
                if (line == "END"):
                    position = location_list[0]
                    location = Location(position, int(location_list[1]), location_list[2], " ".join(location_list[3:-1]))
                    locations[position] = location
                    location_list = []
        for position in locations:
            for start, items in self.items.items():
                for item in items:
                    if position == start:
                        locations[position].items[item.name] = item
        return locations



    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''

        items = {}
        item_file = open(filename, "r")
        for line in item_file:
            line = line.strip().split()
            start = int(line[0])
            target = int(line[1])
            target_points = int(line[2])
            name = " ".join(line[3:])
            item = Item(name, start, target, target_points)
            if (start not in items):
                items[start] = [item]
            else:
                items[start].append(item)
        return items


    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

        int_location = self.map[y][x]
        if (int_location == -1):
            return None
        else:
            return self.locations[int_location]
