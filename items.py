import csv

class Item:
    all = []
    disc_fact = 1

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.__name = name # set as a proprty with __ to indicate read only since there is a property below. Otherwise you get an attribute error
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    ''' set properties which are attributes which are read only, by convention you also add an _ to a property name and __ to prevent access to the property outside the class, 
    by also implementing setter to your properties you can perform logic overriding the read only requirement. Without a setter, the proprty is read only. 
    Note that the _ and __ are just conventions to name things and python doesn't enforce anything
    '''
    @property
    def name(self):
        return self.__name
    
    # sets the name value
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        # this is useful since we can add logic to set the new attribute value, I call it an attribute now in my opinion since we added a setter
        return self.__name
    
    '''encapsulation refers to when you prevent direct access to an attribute by making it a property, but create methods that allow you to modify in pre-defined way
    here we set price as a read only attribute i.e property and only allow the instance methods to change it'''
    def apply_increment(self, increase_fac):
        self.__price += self.__price*increase_fac
        return self.__price
    
    def apply_discount(self, disc):
        self.__price = self.__price * disc * self.disc_fact

    def calculate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for item in items:
                Item(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity'))
                )
    
    @staticmethod
    def isinteger(num):
        if isinstance(num, float):
            # values with .0 are considered int since they are equivalent
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    '''
    abstraction: sometimes we want to seperate out an action into many different methods like sending an email. Therefore, instead of having one email method, 
    we create broken down methods like calling the server, preparing the body of the email, before finally calling all these methods in a final method. 
    This though allows users of the class to access the many broken down methods when we really only want them to have access to the final method which calls all the methods. 
    To abstract the other methods we use the __ double underscore infront of the method so that it is uncallable outside the class.
    '''

    def __connect(self):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
        print("email sent")