from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
is_on = True

while is_on:
    items_list = order.get_items()
    choice = input(f"What would you like? ({items_list}) : ")
    drink = order.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report() 
        money.report() 
    else:
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
        # else: 
        #     coffee.is_resource_sufficient(drink)