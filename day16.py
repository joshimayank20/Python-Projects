class CoffeeMachine:
    def __init__(self):
        self.money = 0
    
    def make_coffee(self, drink, cost):
        print(f"Making {drink}")
        self.money += cost

machine = CoffeeMachine()
machine.make_coffee("latte", 70)
print(machine.money)
