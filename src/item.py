
class Item:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name} is {self.description}'

    def on_take(self):
        print(f'You have picked {self.name}')

    def on_drop(self):
        print(f'You have dropped {self.name}')


class Treasure(Item):
    def __init__(self, amount, name, description=''):
        super().__init__(name, description)
        self.amount = amount


class LightSource(Item):
    def __init__(self, intensity, name, description=''):
        super().__init__(name, description)
        self.intensity = intensity

    def on_drop(self):
        print(f"It's not wise to drop your {self.name}, source of light!")
