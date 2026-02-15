MENU = {
    "espresso": {"cost": 50},
    "latte": {"cost": 70},
    "cappuccino": {"cost": 90}
}

money = 0

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if choice == "off":
        break
    
    if choice in MENU:
        print(f"Please pay ₹{MENU[choice]['cost']}")
        payment = int(input("Insert money: ₹"))
        
        if payment >= MENU[choice]["cost"]:
            change = payment - MENU[choice]["cost"]
            print(f"Here is your {choice}. Change: ₹{change}")
            money += MENU[choice]["cost"]
        else:
            print("Not enough money.")
