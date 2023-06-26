from items import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call super functions to have access to all trributes/methods
        super().__init__(
            name, price, quantity
        )

        # run validations to recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        self.broken_phones = broken_phones
