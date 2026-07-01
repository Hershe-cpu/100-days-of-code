class MenuItem:
    names=[]
    def __init__ (self,name,water,milk,coffee,cost:float,ingredients:dict):
        self.name = name
        self.cost = cost
        self.ingredients = {
                        "water": water,
                        "milk": milk,
                        "coffee": coffee
                    }


        MenuItem.names.append(self.name)


def get_items():
    print(f"Menu Items: {MenuItem.names}")


class Menu:
    def __init__ (self):
        self.menu = [
            MenuItem((name="latte", water=200, milk=150, coffee=24, cost=2.5),)
        ]

