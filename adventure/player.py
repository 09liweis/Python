class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.visited = []
        self.victory = False
        self.score = 0

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx:
        :param dy:
        :return:
        '''
        self.x += dx
        self.y += dy

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map'''
        self.move(0,-1)

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(-1,0)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item:
        :return:
        '''
        self.inventory.append(item)

    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item:
        :return:
        '''
        
        self.inventory.remove(item)

    def get_inventory(self):
        '''
        Return inventory.
        :return:
        '''
        return self.inventory
    
    def visit_location(self, location):
        if (location in self.visited):
            return True
        else:
            self.visited.append(location)
            return False
