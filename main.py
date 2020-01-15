from classes import Pizza

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.
classic_cheese_pizza = Pizza("x-large")
classic_pepp_pizza = Pizza("medium")

# print(classic_cheese_pizza.size)

classic_cheese_pizza.add_topping("parmesan")
classic_cheese_pizza.add_topping("basil")


classic_cheese_pizza.print_order(classic_cheese_pizza.size, classic_cheese_pizza.style, classic_cheese_pizza.toppings)