from items import Item
from phone import Phone
from keyboards import Keyboard

'''
Item.instantiate_from_csv()
print(Item.all)

print(Item.isinteger(1.0))
'''

phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)
item3 = Item("tshirt", 30, 2)

''' diff between static/class/regular method:
static = a method that is related to the class but is not unique per instance
class = methods that relate to the whole class, like producing a specific output based on a method call like calculate the area of a circle
instance method = used to manipulate attributes and properties, like updating the price of a product
'''
#print(Item.all)
#item3.name = "hello"
#print(item3.name)
#print(item3)
#print(item3.apply_increment(2))
item3.send_email()

'''
polymorphism:
the ability of your class to use different logic depending on the object type being used to call. 
For example, when you use len() it will return the length differently when given a list and when given a string. 
Similarly, if I create a Keyboard class that applies discount in a different way than normally, this is called polymorphism.
Here Keyboard objects have an additional 10% discount to whatever discount you apply
'''
keyboard1 = Keyboard("razor", 100, 1)
print(keyboard1)
keyboard1.apply_discount(0.5) # here an additional 0.1 is multiplied to the discount value when object is a Keyboard
print(keyboard1)