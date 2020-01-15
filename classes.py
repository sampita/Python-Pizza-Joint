class Pizza:
    # Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
    def __init__(self, size):
        self.style = "regular"
        self.size = size
        self.toppings = list()

    # Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, topping):
        self.toppings.append(topping)
        
    # Add a method for outputting a description of the pizza (sample output below).
    def print_order(self, size, style, toppings):
        toppings = " and ".join(self.toppings)
        print(f'I would like a {self.size}, {self.style} pizza with {toppings}')