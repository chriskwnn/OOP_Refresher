from items import Item

class Keyboard(Item):
    disc_fact = 0.1
    def __init__(self, name: str, price: float, quantity=0):
        # call super functions to have access to all trributes/methods
        super().__init__(
            name, price, quantity
        )
    