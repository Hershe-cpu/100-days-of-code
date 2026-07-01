class MoneyMachine:

    def __init__ (self):
        pass

def coin_counter():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    money = {"dime": dimes, "quarter": quarters, "nickel": nickles, "penny": pennies}
    total_money = money["dime"] * 0.10 + money["quarter"] * 0.25 + money["nickel"] * 0.05 + money["penny"] * 0.01
    return total_money
