# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.bag = []
        self.score = ''

        def __str__(self):
            return f'{self.name} is in {self.current_room}'

        def add_item(self, item):
            self.items.append(item)

        def is_score(self, point):
            self.score.append(point)
        
        def add_treasure(self, treasure):
            self.bag.append(treasure)

        
