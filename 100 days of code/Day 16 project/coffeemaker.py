class CoffeeMaker:
    """Models the machine that makes up the coffee."""
    drink = input("What is your drink?")

    drink_ingredients = {'Latte': {"water": 300,
                                   "milk": 200,
                                   "coffee": 100
                                   },
                         'Cappuccino': {
                             "water": 300,
                             "milk": 200,
                             "coffee": 100
                         },
                         'Espresso': {
                             "water": 300,
                             "milk": 200,
                             "coffee": 100
                         }, }
    def __init__ (self,drink):
        self.resources={
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        CoffeeMaker.drink_ingredients={'Latte':{"water": 300,
                                                "milk": 200,
                                                "coffee": 100
                                                },
                                       'Cappuccino':{
                                           "water": 300,
                                           "milk": 200,
                                           "coffee": 100
                                       },
                                       'Espresso':{
                                           "water": 300,
                                           "milk": 200,
                                           "coffee": 100
                                       },}

    def report(self):
        """Prints out the coffee report."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def enough_resources(self,drink):
        """Returns True if resources are enough."""
        can_make=True
        for resource in self.resources:
            if CoffeeMaker.drink.ingredients[drink][resource] > self.resources[resource]:
                print(f"Sorry, you don't have enough {resource}.")
                return False
        return True

Coffe=CoffeeMaker("latte")
print(Coffe)