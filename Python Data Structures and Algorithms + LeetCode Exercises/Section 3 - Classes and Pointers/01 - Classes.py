"""Example code on how to define a class in Python."""


class Cookie:
    """A class to model cookies"""
    
    def __init__(self, colour):
        """The constructor method for initializing instaances 
        of the Cookie class with a colour attribute."""
        self.colour = colour

    def get_colour(self):
        """A method to return the colour of a cookie."""
        return self.colour
    
    def set_colour(self, colour):
        """A method to change the colour of a cookie to the specified colour"""
        self.colour = colour



    """Every class has a constructor. The constructor is a special method that 
    is called when an object of the class is created. It's syntax looks like the 
    definition of a regular function but with the name __init__ and it takes and
    the self parameter as its first parameter. The self parameter is a reference to
    the current instance of the class and is used to access variables that belongs.
    
    Functions that are defined inside classes and have the self parameter as 
    their first parameter are called methods."""

cookie_one = Cookie("green")
cookie_two = Cookie("blue")


print(f"Cookie one is: {cookie_one.get_colour()}")
print(f"Cookie two is: {cookie_two.get_colour()}")

cookie_one.set_colour("yellow")

print(f"\nCookie one is now: {cookie_one.get_colour()}")
print(f"Cookie two is still: {cookie_two.get_colour()}")