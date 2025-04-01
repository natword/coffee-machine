import data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}
continu = True

def report(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")

def check_ressource(drink, resources, menu):
    enough = True
    if menu[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water ")
        enough = False
    if drink != "espresso"and menu[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk ")
        enough = False
    if menu[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee ")
        enough = False
    return enough

def insert_coin():
    quarters = int(input("quarters : "))
    dimes = int(input("dimes :"))
    nickles = int(input("nickles :"))
    pennies = int(input("pennies :"))

    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

def transaction(drink, menu, ressource, money_insert):
    if menu[drink]["cost"] > money_insert:
        print("sorry that's not enough money, money refounded !")
        return money_insert
    else:
        change = money_insert - menu[drink]["cost"]
        resources["money"] += menu[drink]["cost"]

        if change > 0:
            print(f"here is the money in change : {round(change, 2)}$")
        return change


def make_coffee(drink, menu, ressource):
    ressource["water"] -= menu[drink]["ingredients"]["water"]
    if drink != "espresso":
        ressource["milk"] -= menu[drink]["ingredients"]["milk"]
    ressource["coffee"] -= menu[drink]["ingredients"]["coffee"]
    print("Here your coffee! enjoy ")


while continu:
    print(r"""
              _____  _____                                     .__    .__               
  ____  _____/ ____\/ ____\____   ____     _____ _____    ____ |  |__ |__| ____   ____  
_/ ___\/  _ \   __\\   __\/ __ \_/ __ \   /     \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\  \__(  <_> )  |   |  | \  ___/\  ___/  |  Y Y  \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \___  >____/|__|   |__|  \___  >\___  > |__|_|  (____  /\___  >___|  /__|___|  /\___  >
     \/                       \/     \/        \/     \/     \/     \/        \/     \/ 
""")
    coffee = input("What would you like ? (espresso, latte, cappuccino ) : ")
    while coffee not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Input error, try again !")
        coffee = input("What would you like ? (espresso, latte, cappuccino ) : ")
    if coffee == "off":
        continu = False
        break
    if coffee == "report":
        report(resources)
    else:
        if check_ressource(coffee, resources, MENU):
            money_insert = insert_coin()
            change = transaction(coffee, MENU, resources, money_insert)
            if change != money_insert:
                make_coffee(coffee, MENU, resources)

